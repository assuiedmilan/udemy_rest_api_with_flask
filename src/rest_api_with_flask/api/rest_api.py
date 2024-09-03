from flask import Flask


class RestApi:
    """This class is responsible for creating the Flask application instance"""

    _rest_app = None

    @staticmethod
    def create_app(force: bool = False) -> Flask:
        """Create a Flask application instance"""
        if RestApi._rest_app is None or force:
            RestApi._rest_app = Flask(__name__)
        return RestApi._rest_app

    @staticmethod
    def rest_app() -> Flask:
        """Get the Flask application instance"""
        return RestApi._rest_app
