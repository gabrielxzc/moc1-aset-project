class IDiskRepository:
    def get_file(self, path: str) -> bytes:
        pass


class DiskRepository(IDiskRepository):
    def get_file(self, path: str) -> bytes:
        in_file = open(path, "rb")
        data = in_file.read()
        in_file.close()

        return data

    def save_file(self, filepath, data: bytes):
        with open(filepath, "wb") as f:
            f.write(data)


if __name__ == "__main__":
    disk_repository = DiskRepository()
    disk_repository.save_file("./file.wav", disk_repository.get_file("../test/data/audio.wav"))
