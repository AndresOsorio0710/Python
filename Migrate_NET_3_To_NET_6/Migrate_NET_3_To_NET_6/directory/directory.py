import errno
import os
from shutil import rmtree
from file import File


class Directory():
    file = File()
    def subdirectory_list(self,path):
        if path == "":
            path="../"
        directories = os.scandir(path)
        return [subdirectory.name for subdirectory in directories if subdirectory.is_dir()]

    def is_proyect(self,path):
        for file in self.file.list_files(path):
            if file.endswith(".csproj"):
                return True
        return False

    def roam_directory(self, path):
        if path == "":
            path="../"
        subdirectory = self.subdirectory_list(path)
        if self.is_proyect(os.path.abspath(path)):
            print(path)
            self.remove_bin_and_obj_directories(path)
        else:
            if len(subdirectory) > 0:
                for directory in subdirectory:
                    if directory != "Migrate_NET_3_To_NET_6":
                        self.roam_directory(f'{os.path.abspath(path)}\{directory}')
        

    def remove_bin_and_obj_directories(self, path):
        try:
            rmtree(f'{path}\\bin')
            rmtree(f'{path}\\obj')
            return "OK"
        except OSError as e:
            return (f"Error:{ e.strerror}")
