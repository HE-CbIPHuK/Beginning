from pathlib import Path
from typing import Optional, Callable


# the contents of the file are divided into tokens, according to the algorithm prescribed in the tokenizer

def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:  # working with folder and file extension
    counter = 0
    for file in dir_path.glob(f'*.{file_extension}'):
        with file.open('r') as f:
            if tokenizer is None:
                counter += len(f.readlines())
            else:
                counter += len(tokenizer('\n'.join(f.readlines())))  # in the counter record the number of tokens
    return counter  # return number of lines of files of a particular type