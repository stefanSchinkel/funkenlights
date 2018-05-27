import json

from funkenlights import create_app
from funkenlights import config
if __name__ == '__main__':
    app = create_app(config)
    app.run(host='0.0.0.0', debug=True)
