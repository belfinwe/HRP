import configparser
import logging

# Version
__version__ = "0.1.2"

# Database connection
config = configparser.ConfigParser()
config.read("secret_config.ini")
db_cfg = config["database"]

pg_db_user = db_cfg["user"]
pg_db_password = db_cfg["password"]
pg_db_postgresserver = f"""{db_cfg["password"]}:{db_cfg["port"]}"""
pg_db_name = db_cfg["db_name"]
pg_db_driver = db_cfg["driver"]

SQLALCHEMY_DATABASE_URL = f"{pg_db_driver}://{pg_db_user}:{pg_db_password}@{pg_db_postgresserver}/{pg_db_name}"

# Log
__format = "%(asctime)s - %(funcName)s: %(message)s"
logging.basicConfig(format=__format, level=logging.INFO)
