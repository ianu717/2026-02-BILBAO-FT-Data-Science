import os
from functions import create_folders, organize_files
PATH_DOWNLOADS = 'C:\\Users\\unai7\\Downloads\\Daunloads'

def main():
    os.chdir(PATH_DOWNLOADS)
    create_folders()
    organize_files()

if __name__ == '__main__':
    main()

