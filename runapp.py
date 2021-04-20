import os
import logging

from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app = loadapp('config:production.ini', relative_to='.')
    logging.warning('just a simple warning message')

    serve(app, host='0.0.0.0', port=port)
