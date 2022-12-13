import os


class Css2String:

    @staticmethod
    def read(a_sPath:str|bytes)-> str:
        abspath = os.path.abspath(a_sPath)
        if os.path.isfile(abspath):
            file = open(abspath)
            if file:
                content = file.read().replace('\n', ' ')
                return content
        raise FileNotFoundError('File not found or corrupted')

    @staticmethod
    def validate_extension(a_sPath:str|bytes)-> bool:
        abspath = os.path.abspath(a_sPath)
        if abspath.endswith('.css'):
            return True
        return False

