from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

user = "root"
password = "krlospk"
port = "3306"
db_name = "dragones_python"

connection_db = f"mysql+mysqlconnector://{user}:{password}@localhost:{port}/{db_name}"

engine = create_engine(connection_db, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@event.listens_for(Engine, "connect")
def set_sql_mode(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    cursor.close()
