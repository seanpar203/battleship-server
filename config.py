""" Module to handle different settings for different environments. """
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Base configuration class that provide attrs unique to certain envs

    Attributes:
            DEBUG (bool): Enables or disables debugging mode.
            TESTING (bool): Enables testing mode.
            CSRF_ENABLED (bool): Enables CSRF Tokens.
            SECRET_KEY (str): Secret key for application.
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProdConfig(Config):
    """ Production settings class, inherits from Config.

    Attributes:
            DEBUG (bool): Enables or disables debugging mode.
    """
    DEBUG = False


class StageConfig(Config):
    """ Staging settings class, inherits from Config.

    Attributes:
        DEBUG (bool): Enables or disables debugging mode.
        DEVELOPMENT (bool): Enables development mode.
    """
    DEBUG = True
    DEVELOPMENT = True


class DevConfig(Config):
    """ Development settings class, inherits from Config.

    Attributes:
            DEBUG (bool): Enables or disables debugging mode.
            DEVELOPMENT (bool): Enables development mode.
    """
    DEBUG = True
    DEVELOPMENT = True


class TestConfig(Config):
    """ Testing settings class, inherits from Config.

    Attributes:
            TESTING (bool): Enables or disables testing mode.
    """
    TESTING = True
