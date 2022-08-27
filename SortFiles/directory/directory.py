import os

from file import File


class Directory():
    file = File()
    EXCLUDED_DIRECTORIES = ['VENV','DIRECTORY','FILE','ORGANIZED']

    def list_directory(self):
        subdirectorys = os.scandir()
        return [subdirectory.name for subdirectory in subdirectorys if subdirectory.is_dir()]
    

    def roam_directory(self):
        for directory_name in self.list_directory():
            if not (directory_name.upper() in self.EXCLUDED_DIRECTORIES):
                print(f'Init Directory "{directory_name}"')
                self.file.sort_file(os.path.abspath(directory_name))
                print(f'End Directory "{directory_name}"')
