import sys
from directory import Directory
from file import File

directory = Directory()
file = File()

def main():
    print("Migrate .NET 3.X To .NET 6.X")
    directory.roam_directory("")


if __name__ == '__main__':
    sys.exit(main())