class IDiskRepository:
    def get_file(self, path: str) -> bytes:
        pass


class DiskRepository(IDiskRepository):
    def get_file(self, path: str) -> bytes:
        in_file = open(path, "rb")
        data = in_file.read()
        in_file.close()

        return data
