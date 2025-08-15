import argparse


from organizer import sort_by_extension, sort_by_size, sort_by_date

main_parser = argparse.ArgumentParser(
    prog="Terminal Sort",
    description='A CLI tool to sort your files',
    epilog='This is a tool that sorts all the files in a directory and subdirectory, and also tracks the changes made for future undo actions.'
    
)

main_parser.add_argument('--by', type=str, required=True, help='What do you want to sort this folder by?')
main_parser.add_argument('--path', type=str, required=True, default='./', help='Directory path to the files')

args = main_parser.parse_args()

match args.by:
    case "extension" | "e":
        sort_by_extension(args.path)
    case "date" | "d":
        sort_by_date(args.path)
        ...
    case "size" | "s":
        sort_by_size(args.path)
    case _:
        print(f"Invalid option: {args.by}\nUse extension or e , date or d, size or s, to sort the folder")

