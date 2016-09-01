""" Module that handles all the routes for the web-time-analytics extension."""
from wta_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
