import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy_batch_inserts import enable_batch_inserting
from sqlalchemy_utils import database_exists, create_database

from orm.entities import *
from utils.constants import URL_TO_DATABASE

warnings.filterwarnings("ignore")


class DbConnection:
    def __init__(self):
        pass

    def make_connection(self):
        url = URL_TO_DATABASE
        if not database_exists(url):
            create_database(url)

        # configs and instances
        engine = sqlalchemy.create_engine(URL_TO_DATABASE)
        return engine

    def create_tables(self, engine):
        Session = sessionmaker(bind=engine)

        # create a Session
        session = Session()
        enable_batch_inserting(session)

        # create all tables, if not existent already
        Base.metadata.create_all(engine)
        return session


def try_simple_operation_in_database():
    dbConnection = DbConnection()
    engine_db_connection = dbConnection.make_connection()

    session = dbConnection.create_tables(engine=engine_db_connection)
    session.add(Label(label_name="Bark"))
    session.commit()

    labels_elem = session.query(Label).all()
    for label in labels_elem:
        print(label.label_name)

    print("Inserted in audio-tagging Database.")


if __name__ == "__main__":
    try_simple_operation_in_database()
