class FileValueError(Exception):
    pass


class KeyValueStorage:  # class that decorates the file
    """the class wraps a file and provide values as attributes"""

    def __setitem__(self, key, item):  # methods for accessing an attribute through square brackets
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __init__(self, path: str):  # define instantiation
        with open(path, 'r') as file:  # open file
            for line in file:
                try:  # checking if the key is a number
                    int(line.split('=')[0])
                    raise FileValueError('Key can not be an integer.')
                except ValueError:  # processing if not
                    key = line.split('=')[0]
                    try:
                        value = int(line.split('=')[1])
                    except ValueError:
                        value = line.split('=')[1].strip()
                    if key not in dir(self):  # checking the originality of an attribute to create it
                        setattr(self, key, value)
                        self[key] = value