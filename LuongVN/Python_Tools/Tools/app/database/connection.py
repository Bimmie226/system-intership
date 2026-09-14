from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings

DATABASE_URL = (f"mysql+pymysql://{settings.DB_USER}:" f"{settings.DB_PASSWORD}@" f"{settings.DB_HOST}:" f"{settings.DB_PORT}/" f"{settings.DB_NAME}")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            value = result.scalar()

            print("Kết nối MariaDB thành công")
            print("SELECT 1 =", value)

    except Exception as e:
        print("Kết nối MariaDB thất bại")
        print(e)


if __name__ == "__main__":
    test_connection()