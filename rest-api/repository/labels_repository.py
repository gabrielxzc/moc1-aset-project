import pandas as pd

from orm.db_connection_manager import DbConnection
from orm.entities import Label
from utils.constants import URL_TO_DATABASE


class LabelRepository:
    def __init__(self):
        dbConnection = DbConnection()
        engine_db_connection = dbConnection.make_connection()
        self.session = dbConnection.create_tables(engine_db_connection)

    def add(self, label_name):
        label = Label(label_name)
        self.session.add(label)

    def commit(self):
        self.session.commit()

    def find_by_id(self, id):
        return self.session.query(Label).get(id)

    def find_by_label_name(self, label_name):
        return self.session.find(Label).filter_by(label_name=label_name).first()

    def get_all(self):
        return pd.read_sql_table(Label.__tablename__, URL_TO_DATABASE)

    def update(self, id, label_name):
        label = self.find_by_id(id)
        label.label_name = label_name
        self.session.add(label)

    def delete(self, id):
        label = self.find_by_id(id)
        self.session.delete(label)

    def insert_or_update(self, label_name):
        self.add(label_name) if self.find_by_label_name(
            label_name) is None else self.update(id, label_name)
