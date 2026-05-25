#[macro_use]
extern crate rocket;

use rocket::State;
use rocket::form::Form;
use rocket::http::ContentType;
use rocket::response::status::NotFound;
use rocket::serde::json::Json;
use rocket_dyn_templates::{Template, context};
use serde::Deserialize;
use serde_json::json;
use std::fs;
use std::process::Command;

use include_dir::{Dir, include_dir};

#[derive(Debug, Clone, Deserialize)]
struct Config {
    binaries: Binaries,
    devices: Vec<Device>,
}

#[derive(Debug, Clone, Deserialize)]
struct Binaries {
    send: Option<String>,
    codesend: String,
    sniff: Option<String>,
}

#[derive(Debug, Clone, Deserialize, serde::Serialize)]
struct Device {
    name: String,
    on: u32,
    off: u32,
}

#[derive(FromForm)]
struct SendForm {
    code: String,
}

static STATIC_DIR: Dir<'_> = include_dir!("$CARGO_MANIFEST_DIR/funkenlights/static");
static TEMPLATE_DIR: Dir<'_> = include_dir!("$CARGO_MANIFEST_DIR/templates");

#[get("/")]
fn index(cfg: &State<Config>) -> Template {
    Template::render("main", context! { devices: &cfg.devices })
}

#[get("/static/<path..>")]
fn static_files(path: std::path::PathBuf) -> Result<(ContentType, Vec<u8>), NotFound<String>> {
    let path_str = path.to_string_lossy();
    let file = STATIC_DIR
        .get_file(path_str.as_ref())
        .ok_or_else(|| NotFound("static file not found".to_string()))?;
    let content_type = file
        .path()
        .extension()
        .and_then(|ext| ext.to_str())
        .and_then(ContentType::from_extension)
        .unwrap_or(ContentType::Binary);
    Ok((content_type, file.contents().to_vec()))
}

#[post("/send", data = "<form>")]
fn send(cfg: &State<Config>, form: Form<SendForm>) -> Json<serde_json::Value> {
    let status = Command::new(&cfg.binaries.codesend)
        .arg(&form.code)
        .status();

    let ret_code = status.ok().and_then(|st| st.code()).unwrap_or(-1);

    Json(json!({ "res": ret_code }))
}

#[get("/health")]
fn health() -> Json<serde_json::Value> {
    Json(json!({ "status": "ok" }))
}

fn load_config() -> Config {
    let raw = fs::read_to_string("config.json")
        .or_else(|_| fs::read_to_string("config.sample.json"))
        .expect("config.json or config.sample.json must exist");
    serde_json::from_str(&raw).expect("config JSON is invalid")
}

#[launch]
fn rocket() -> _ {
    let cfg = load_config();

    let templates = TEMPLATE_DIR
        .get_file("main.html.tera")
        .expect("templates/main.html.tera missing");
    let template_source = String::from_utf8_lossy(templates.contents()).to_string();

    rocket::build()
        .manage(cfg)
        .mount("/", routes![index, send, health, static_files])
        .attach(Template::custom(move |engines| {
            engines
                .tera
                .add_raw_template("main", template_source.as_str())
                .expect("failed to register template");
        }))
}
