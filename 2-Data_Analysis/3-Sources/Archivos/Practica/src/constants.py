from enum import Enum

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')
compressed_types = ('.zip', '.rar', '.tar', '.gz', '.7z')
audio_types = ('.mp3', '.wav', '.aac', '.flac')
video_types = ('.mp4', '.avi', '.mkv', '.mov', )

class FolderNames(Enum):
    DOCUMENTS = 'Documentos'
    IMAGES = 'Imagenes'
    SOFTWARE = 'Software'
    COMPRESSED = 'Comprimidos'
    AUDIO = 'Audio'
    VIDEO = 'Video'
    OTHERS = 'Otras'

    @classmethod
    def get_values(cls):
        return [value.value for key, value in cls.__members__.items()]