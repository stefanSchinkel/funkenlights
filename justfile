set dotenv-load := true
set dotenv-path := ".env"

alias b := build
alias bp := build-pi
alias bpr := build-pi-release

alias dd := deploy-dev
alias dp := deploy-prod

alias ds := deploy-static
run:
  cargo run

test:
  cargo test

build:
  cargo build

# build release version
build-release:
  cargo build --release

build-pi:
  cargo build --target=armv7-unknown-linux-musleabihf

build-pi-release:
  cargo build --release --target=armv7-unknown-linux-musleabihf

# deploy dev version
deploy-dev:
 scp target/armv7-unknown-linux-musleabihf/debug/funkenlights ${RPI_USER}@${RPI}:${RPI_PATH}/

# deploy prod version
deploy-prod:
 scp target/armv7-unknown-linux-musleabihf/release/funkenlights ${RPI_USER}@${RPI}:${RPI_PATH}/


# deploy statics
deploy-static:
 scp -r templates/ ${RPI_USER}@${RPI}:${RPI_PATH}/
