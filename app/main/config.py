import os
from types import NoneType
from dotenv import load_dotenv

load_dotenv()

postgres_local_base =os.getenv("DATABASE_URL")
db_name = os.getenv("RDS_DB_NAME", None)
rds_username = os.getenv("RDS_USERNAME", None)
rds_password = os.getenv("RDS_PASSWORD", None)
rds_port = os.getenv("RDS_PORT", None)
rds_host_name = os.getenv("RDS_HOSTNAME", None)
basedir = os.path.abspath(os.path.dirname(__file__))

# prod_database_uri= f"postgresql://{rds_username}:{rds_password}@{rds_host_name}:{rds_port}/{db_name}"

class Config:
    SECRET_KEY= os.getenv("SECRET_KEY", "DGGKEIEOMACVNNETKAAMFBfbn")
    DEBUG = False
    ERROR_PATH =os.getenv('ERROR_PATH', None)

class DevelopmentConfig(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, "flask_boilerplate_test.db")
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = True
   

config_by_name = dict(
    development= DevelopmentConfig,
    test = TestingConfig,
    production = ProductionConfig
)

SECRET_KEY = Config.SECRET_KEY
SECURITY_PASSWORD_SALT= os.getenv("SECURITY_PASSWORD_SALT")
ALGORITHM=os.getenv("ALGORITHM")

