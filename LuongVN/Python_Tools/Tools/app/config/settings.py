import os
from dotenv import load_dotenv

load_dotenv() 

class Settings: 
    K8S_CONFIG_MODE = os.getenv("K8S_CONFIG_MODE")
    KUBERNETES_PATH = os.getenv("KUBERNETES_PATH")
    
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    
settings = Settings()
