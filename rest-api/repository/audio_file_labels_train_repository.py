import pandas as pd

from orm.db_connection_manager import DbConnection
from orm.entities import AudioFileLabelsTrain
from utils.constants import URL_TO_DATABASE


class AudioFileLabelsTrainRepository:
    def __init__(self):
        dbConnection = DbConnection()
        engine_db_connection = dbConnection.make_connection()
        self.session = dbConnection.create_tables(engine_db_connection)

    def add(self, audio_file_id, label_id):
        audio_file = AudioFileLabelsTrain(audio_file_id, label_id)
        self.session.add(audio_file)

    def commit(self):
        self.session.commit()

    def find_by_id(self, id):
        return self.session.query(AudioFileLabelsTrain).get(id)

    def find_by_pair_of_ids(self, audio_file_id, label_id):
        return (
            self.session.query(AudioFileLabelsTrain)
            .filter_by(label_id=label_id)
            .filter_by(audio_file_id=audio_file_id)
            .first()
        )

    def get_all(self):
        return pd.read_sql_table(AudioFileLabelsTrain.__tablename__, URL_TO_DATABASE)

    def update(self, id, audio_file_id, label_id):
        audio_label_instance = self.find_by_id(id)
        audio_label_instance.audio_file_id, label_id = audio_file_id, label_id
        self.session.add(audio_label_instance)

    def delete(self, id):
        audio_label_instance = self.find_by_id(id)
        self.session.delete(audio_label_instance)

    def insert_or_update(self, audio_file_id, label_id):
        self.add(audio_file_id, label_id) if self.find_by_pair_of_ids(
            audio_file_id, label_id
        ) is None else self.update(id, audio_file_id, label_id)
