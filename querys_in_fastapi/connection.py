import pymysql
import os
from dotenv import load_dotenv
from logger import log_event


load_dotenv()

class Connection:
    def __init__(self):
        log_event("INFO", "Initializing Database configuration")
        self.config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "port": int(os.getenv("DB_PORT", 3306)),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME", "digital_hunter"),
            "cursorclass": pymysql.cursors.DictCursor 
        }
        log_event("INFO", f"Database config loaded for host: {self.config['host']}, user: {self.config['user']}")

    def get_connection(self):
        try:
            connection = pymysql.connect(**self.config)
            log_event("INFO", "Successfully established connection to MySQL")
            return connection
        except Exception as e:
            log_event("ERROR", f"Failed to connect to MySQL: {str(e)}")
            raise e


connection = Connection()