class IDiskRepository:
    def get_file(self, path: str) -> bytes:
        pass


class DiskRepository(IDiskRepository):
    def get_file(self, path: str) -> bytes:
        in_file = open(r"D:\moc1-aset-project\data\sounds\train_curated\00b0b76f.wav", "rb")
        data = in_file.read()
        in_file.close()

        return data
