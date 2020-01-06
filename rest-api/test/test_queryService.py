from unittest import TestCase

from orm.entities import Label, UploadedAudioFile
from service.query_service import QueryService


class DummyRepository:
    def find_by_label_name(self, label):
        if label == "abc":
            _label = Label(label)
            _label.description = "test"

            audio_file1 = UploadedAudioFile("/dev/file.wav", "test")
            audio_file1.id = 1

            audio_file2 = UploadedAudioFile("/dev/file2.wav", "test1")
            audio_file2.id = 2

            _label.audio_files = [audio_file1, audio_file2]

            return _label
        elif label == "12":
            _label = Label(label)
            _label.description = "test2"
            audio_file1 = UploadedAudioFile("/dev/file3.wav", "test2")
            audio_file1.id = 3

            audio_file2 = UploadedAudioFile("/dev/file2.wav", "test1")
            audio_file2.id = 4

            _label.audio_files = [audio_file1, audio_file2]

            return _label


class TestQueryService(TestCase):
    QUERY = "abc,def,gh.,12"

    def setUp(self) -> None:
        self.query_service = QueryService(DummyRepository())

    def test_extract_labels(self):
        labels = self.query_service.extract_labels(self.QUERY)
        assert labels == ["abc", "def", "gh.", "12"]

    def test_get_metadata(self):
        expected_result = {
            "metadata": [
                {"id": 1, "description": "test", "labels": []},
                {"id": 2, "description": "test1", "labels": []},
                {"id": 3, "description": "test2", "labels": []},
                {"id": 4, "description": "test1", "labels": []},
            ]
        }
        metadata = self.query_service.get_metadata(self.QUERY)

        assert metadata == expected_result
