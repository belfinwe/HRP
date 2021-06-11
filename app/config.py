import configparser
import logging

# Version
__version__ = "0.1.2"

# Database connection
config = configparser.ConfigParser()
config.read("secret_config.ini")
db_cfg = config["database"]

__pg_db_user = db_cfg["user"]
__pg_db_password = db_cfg["password"]
__pg_db_postgresserver = f"""{db_cfg["ip"]}:{db_cfg["port"]}"""
__pg_db_name = db_cfg["db_name"]
__pg_db_driver = db_cfg["driver"]

SQLALCHEMY_DATABASE_URL = f"{__pg_db_driver}://{__pg_db_user}:{__pg_db_password}@{__pg_db_postgresserver}/{__pg_db_name}"

# Log
__format = "%(asctime)s - %(funcName)s: %(message)s"
logging.basicConfig(format=__format, level=logging.INFO)
