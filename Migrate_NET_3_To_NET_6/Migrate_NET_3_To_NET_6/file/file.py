import os


class File():
    def list_files(self, path):
        files = []
        if path == "":
            files = os.scandir("../")
        else:
            files = os.scandir(path)
        return [file.name for file in files if file.is_file()]
