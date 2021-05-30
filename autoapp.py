# -*- coding: utf-8 -*-
"""Create an application instance."""
from networks.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"])