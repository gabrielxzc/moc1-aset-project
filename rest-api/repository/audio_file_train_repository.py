import pandas as pd

from orm.db_connection_manager import DbConnection
from orm.entities import AudioFileTrain
from utils.constants import URL_TO_DATABASE


class AudioFileTrainRepository:
    def __init__(self):
        dbConnection = DbConnection()
        engine_db_connection = dbConnection.make_connection()
        self.session = dbConnection.create_tables(engine_db_connection)

    def add(self, file_path):
        audio_file = AudioFileTrain(file_path)
        self.session.add(audio_file)

    def commit(self):
        self.session.commit()

    def find_by_id(self, id):
        return self.session.query(AudioFileTrain).get(id)

    def find_by_file_path(self, file_path):
        return self.session.query(AudioFileTrain).filter_by(file_path=file_path).first()

    def get_all(self):
        return pd.read_sql_table(AudioFileTrain.__tablename__, URL_TO_DATABASE)

    def update(self, id, file_path):
        audio_file = self.find_by_id(id)
        audio_file.file_path = file_path
        self.session.add(audio_file)

    def delete(self, id):
        audio_file = self.find_by_id(id)
        self.session.delete(audio_file)

    def insert_or_update(self, file_path):
        self.add(file_path) if self.find_by_file_path(
            file_path
        ) is None else self.update(id, file_path)
