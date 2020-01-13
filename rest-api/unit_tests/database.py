import unittest

from repository.labels_repository import LabelRepository


class DatabaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.label_repository = LabelRepository()
        self.test_label_name = "mock_label"

        if self.label_repository.find_by_label_name(self.test_label_name) is None:
            self.label_repository.add(self.test_label_name)
            self.label_repository.commit()

    def test_find_by_name(self):
        label_obj = self.label_repository.find_by_label_name(self.test_label_name)
        assert label_obj is not None
        assert label_obj.label_name == self.test_label_name

    def test_insert(self):
        test_label_to_add = "mock_label_2"

        self.label_repository.add(test_label_to_add)
        self.label_repository.commit()

        label_obj = self.label_repository.find_by_label_name(test_label_to_add)
        assert label_obj is not None
        assert label_obj.label_name == test_label_to_add

        self.label_repository.delete(label_obj.id)
        self.label_repository.commit()

    def test_duplicate_insert(self):
        try:
            self.label_repository.add(self.test_label_name)
            assert False
        except:
            pass


if __name__ == "__main__":
    unittest.main()
