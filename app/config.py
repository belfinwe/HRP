import configparser
import logging

# Version
__version__ = "0.1.2"

# Database connection
config = configparser.ConfigParser()
config.read("secret_config.ini")

user = config["user"]
password = config["password"]
postgresserver = f"""{config["password"]}:{config["port"]}"""
db = config["db_name"]
driver = config["driver"]

SQLALCHEMY_DATABASE_URL = f"{driver}://{user}:{password}@{postgresserver}/{db}"

# Log
__format = "%(asctime)s - %(funcName)s: %(message)s"
logging.basicConfig(format=__format, level=logging.INFO)
