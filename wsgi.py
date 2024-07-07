import json

from funkenlights import create_app

with open("config.json") as fp:
    cfg = json.load(fp)
    app = create_app(cfg)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
