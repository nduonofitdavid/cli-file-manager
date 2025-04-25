import argparse
import os
import shutil

from  myutils import get_extensions, make_folders
from organizer import sort_by_folder


main_parser = argparse.ArgumentParser(
    prog="David Nduonofit's Sort",
    description='A CLI tool to sort your files',
    epilog='Yeah this is an epilog, you get the idea'
)

main_parser.add_argument('-o', '--organize', action='store_true')
main_parser.add_argument('--by', type=str, required=True, help='What do you want to sort the files by?')
main_parser.add_argument('--path', type=str, required=True, default='./', help='Directory path to the files')

args = main_parser.parse_args()


def main():
    match args.by:
        case "extension":
            folder = os.listdir(args.path)
            directory = args.path   
            extensions = get_extensions(folder)

            if make_folders(extensions, directory):
                sort_by_folder(folder, directory)
                print("operation successful")
        case _:
            raise ValueError


if __name__ == '__main__':
    main()