import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = os.getenv("DB_HOST", "localhost")  # Predeterminado para desarrollo
DB_PORT = os.getenv("DB_PORT", "3315")        # Predeterminado para desarrollo
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "admin")
DB_NAME = os.getenv("MYSQL_DATABASE", "josnishop") # Nombre de la BD

# connection string
# represenat la base de datos a conectar
# dependiendo la base de datos que se use y el lenguaje de programación
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:admin@localhost:3315/josnishop"

# crea el objeto de conexion (permite conectarse a la base de datos)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
