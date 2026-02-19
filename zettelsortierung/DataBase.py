import os
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    connection_string = os.getenv('DATABASE_CONNECTION_STRING')
    return create_engine(connection_string)

def get_metadata():
    return MetaData()