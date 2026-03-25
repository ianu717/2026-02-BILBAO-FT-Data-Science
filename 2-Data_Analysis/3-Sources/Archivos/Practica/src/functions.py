import os
import shutil
from constants import (
    FolderNames, 
    doc_types, 
    img_types, 
    software_types, 
    compressed_types, 
    audio_types, 
    video_types
)

def create_folders():
    for folder_name in FolderNames.get_values():
        os.makedirs(folder_name, exist_ok=True)

def organize_files():
    for file in os.listdir():
        if os.path.isfile(file):
            extension = os.path.splitext(file)[1].lower()
            if extension in doc_types:
                shutil.move(file, os.path.join(FolderNames.DOCUMENTS.value, file))
            elif extension in img_types:
                shutil.move(file, os.path.join(FolderNames.IMAGES.value, file))
            elif extension in software_types:
                shutil.move(file, os.path.join(FolderNames.SOFTWARE.value, file))
            elif extension in compressed_types:
                shutil.move(file, os.path.join(FolderNames.COMPRESSED.value, file))
            elif extension in audio_types:
                shutil.move(file, os.path.join(FolderNames.AUDIO.value, file))
            elif extension in video_types:
                shutil.move(file, os.path.join(FolderNames.VIDEO.value, file))
            else:
                shutil.move(file, os.path.join(FolderNames.OTHERS.value, file))
                