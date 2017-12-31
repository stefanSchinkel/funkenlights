import json

from funkenlights import create_app

with open("config.json") as fp:
    cfg = json.load(fp)

if __name__ == '__main__':
    app = create_app(cfg)