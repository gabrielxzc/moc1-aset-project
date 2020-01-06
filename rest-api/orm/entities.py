import warnings

from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, Table
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Index

warnings.filterwarnings("ignore")

Base = declarative_base()


class AudioFileTrain(Base):
    __tablename__ = "audio_files_train"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    filepath = Column(VARCHAR)
    label_files = relationship("AudioFileLabelsTrain")

    def __init__(self, filepath):
        self.filepath = filepath


class AudioFileLabelsTrain(Base):
    __tablename__ = "audio_file_labels"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    audio_file_id = Column(ForeignKey("audio_files_train.id"))
    label_id = Column(ForeignKey("labels.id"))
    UniqueConstraint(audio_file_id, label_id, name="audio_label_ids_pair_constraint")
    Index("audio_label_idx", audio_file_id, label_id)
    label = relationship("Label")

    def __init__(self, audio_file_id, label_id):
        self.audio_file_id = audio_file_id
        self.label_id = label_id


association_table = Table(
    "predicted_label_for_uploaded_audio",
    Base.metadata,
    Column("audio_file_id", Integer, ForeignKey("uploaded_audio_files.id")),
    Column("label_id", Integer, ForeignKey("labels.id")),
)


class UploadedAudioFile(Base):
    __tablename__ = "uploaded_audio_files"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    filepath = Column(VARCHAR)
    description = Column(VARCHAR)
    label_files = relationship("Label", secondary=association_table)

    def __init__(self, filepath):
        self.filepath = filepath


class Label(Base):
    __tablename__ = "labels"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    label_name = Column(VARCHAR)
    audio_files = relationship("UploadedAudioFile", secondary=association_table)
    UniqueConstraint(label_name, name="label_unique")

    def __init__(self, label_name):
        self.label_name = label_name
