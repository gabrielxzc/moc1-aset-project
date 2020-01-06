import pandas as pd

from orm.db_connection_manager import DbConnection
from orm.entities import UploadedAudioFile
from utils.constants import URL_TO_DATABASE
from orm.entities import UploadedAudioFile


class UploadedAudioFileRepository:
    def __init__(self):
        dbConnection = DbConnection()
        engine_db_connection = dbConnection.make_connection()
        self.session = dbConnection.create_tables(engine_db_connection)

    def add(self, file_path):
        audio_file = UploadedAudioFile(file_path)
        self.session.add(audio_file)

    def commit(self):
        self.session.commit()

    def find_by_id(self, id):
        return self.session.query(UploadedAudioFile).get(id)

    def find_by_file_path(self, file_path):
        return self.session.query(UploadedAudioFile).filter_by(file_path=file_path).first()

    def get_all(self):
        return pd.read_sql_table(UploadedAudioFile.__tablename__, URL_TO_DATABASE)

    def update(self, id, file_path):
        audio_file = self.find_by_id(id)
        audio_file.file_path = file_path
        self.session.add(audio_file)

    def delete(self, id):
        audio_file = self.find_by_id(id)
        self.session.delete(audio_file)

    def insert_or_update(self, file_path):
        self.add(file_path) if self.find_by_file_path(
            file_path) is None else self.update(id, file_path)

# if __name__ == '__main__':
#     upload_audio_file_repository = UploadedAudioFileRepository()
#     upload_audio_file_instance = UploadedAudioFile(filepath="C://blahblah...")
#     upload_audio_file_repository.insert_or_update(upload_audio_file_instance)
#     upload_audio_file_repository.commit()
