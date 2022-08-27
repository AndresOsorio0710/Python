import errno
import os
import sys
from directory import Directory
from file import File


file = File()
directory = Directory()


def create_directory_organized():
    try:
        os.makedirs('Organized/TXT', exist_ok=True)
        os.makedirs('Organized/IMG', exist_ok=True)
        os.makedirs('Organized/AUDIO', exist_ok=True)
        os.makedirs('Organized/DOCUMENTS', exist_ok=True)
        os.makedirs('Organized/VIDEO', exist_ok=True)
        os.makedirs('Organized/OTHERS', exist_ok=True)
        print('Directory "Organized" successfully created')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def main():
    print("Sort Files")
    create_directory_organized()
    directory.roam_directory()


if __name__ == '__main__':
    sys.exit(main())
