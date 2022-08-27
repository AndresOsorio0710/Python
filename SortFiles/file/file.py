import os
import shutil


class File():
    IMG = ['.BMP', '.RAW', '.RAW', '.TIF', '.PNG', '.JPG', '.JPEG', '.GIF',
           '.TIFF', '.PSD', '.EPS', '.PIC', '.SVG', '.AI', '.DWG', ]
    AUDIO = ['.WAV', '.AIFF', '.AU', '.FLAC', '.MPEG-4', '.TTA', '.ATRAC',
             '.MP3', '.VORBIS', '.AAC', '.WMA', '.OGG', '.DSD', '.MQA']
    VIDEO = ['.MP4', '.AVI', '.MKV', '.FLV', '.MOV',
             '.WMV', '.DIVX', '.H.264', '.XVID', '.RM']
    DOCUMENTS = ['.DOC', '.DOCX', '.DOT', '.XLS', '.XLSX',
                 '.XLSM', '.XLT', '.PPT', '.PPTX', '.PPS', '.POT', '.PDF']

    def list_files(self):
        files = os.scandir()
        return [file.name for file in files if file.is_file()]

    def list_files_path(self, path):
        files = os.scandir(path)
        return [file.name for file in files if file.is_file()]

    def sort_file(self, path):
        for file in self.list_files_path(path):
            root, extension = os.path.splitext(self.get_path(file))
            file_identified = False
            if extension == '.txt':
                shutil.copy(os.path.abspath(
                    f'{path}/{file}'), os.path.abspath('Organized/TXT'))
                file_identified = True
            if extension.upper() in self.IMG:
                shutil.copy(os.path.abspath(
                    f'{path}/{file}'), os.path.abspath('Organized/IMG'))
                file_identified = True
            if extension.upper() in self.AUDIO:
                shutil.copy(os.path.abspath(
                    f'{path}/{file}'), os.path.abspath('Organized/AUDIO'))
                file_identified = True
            if extension.upper() in self.DOCUMENTS:
                shutil.copy(os.path.abspath(
                    f'{path}/{file}'), os.path.abspath('Organized/DOCUMENTS'))
                file_identified = True
            if extension.upper() in self.VIDEO:
                shutil.copy(os.path.abspath(
                    f'{path}/{file}'), os.path.abspath('Organized/VIDEO'))
                file_identified = True
            if file_identified == False:
                shutil.copy(os.path.abspath(
                    f'{path}/{file}'), os.path.abspath('Organized/OTHERS'))

    def get_path(self, file_name):
        return os.path.abspath(file_name)
