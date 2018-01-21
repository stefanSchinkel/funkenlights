import json

from funkenlights import create_app

if __name__ == '__main__':
with open("config.json") as fp:
    app = create_app(json.load(fp))