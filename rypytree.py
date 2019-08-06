import pathlib
import argparse
import logging


def create_parser():

    parser = argparse.ArgumentParser(
        description='A program to list all the files and directories ' +
                    'in the specified directory. If no directory is specified, ' +
                    'the current directory will be used.',
        prog='PROG')
    parser.add_argument('directory', metavar='/path/to/dir')
    parser.add_argument('-a', action='store_true')
    parser.add_argument('-f', action='store_true')
    return parser


'''
TODO: 
Save the data into a Dictionary of Dictionaries.
Maybe add depth?
Figure out how to add the tree-like display with the pipes.

'''
def how_far(dir, hidden):
    if dir.is_dir():
        items_in_folder = [item for item in dir.iterdir()]
        for item in items_in_folder:
            if (item.name).startswith('.') and not hidden:
                pass
            elif item.is_dir():
                how_far(item,hidden)
                print('Dir: {}'.format(item))
            else:
                logging.debug('This file is not a directory.')
                print('File: {}'.format(item))
    else:
        logging.debug('This file is not a directory.')
        return None


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    print(args)
    p = pathlib.Path(args.directory)
    how_far(p, args.a)