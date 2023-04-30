
from itertools import tee
from os import system
from pathlib import Path
from re import compile, match


def get_latest_empty_file(folder:Path) -> Path:
    """traverses the directory and gets the first available file"""
    FILENAME_PATTERN = compile("lecture_*[0-9].py")
    pyfiles = filter(lambda x: x.suffix==".py", folder.iterdir())
    pyfiles = filter(lambda x: match(pattern=FILENAME_PATTERN, string=x.name), pyfiles)
    pyf1, pyf2 = tee(pyfiles, 2)
    pyfiles = filter(lambda x: x.read_text()=="", pyf1)
    file_number = min((int(x.name[8:-3]) for x in pyfiles), default=None)
    if file_number is None:
        pyfiles = filter(lambda x: x.read_text()!="", pyf2)
        last_full = max((int(x.name[8:-3]) for x in pyfiles))
        file_number = last_full + 1
    return folder / f"lecture_{file_number}.py"


def main():
    _ = system("cls")
    folder = Path(__file__).parent
    new_file = get_latest_empty_file(folder)
    new_file.touch()
    print(new_file)
    
    return 0


if __name__ == "__main__":
    main()