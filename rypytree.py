import pathlib
import argparse

LINES = '│  '
SPACE = '   '


def create_parser():
    parser = argparse.ArgumentParser(
        description='a program to list all the files and directories ' +
                    'in the specified directory. If no directory is specified, ' +
                    'the current directory will be used.',
        prog='rypytree.py')
    parser.add_argument('directory', metavar='/path/to/dir')
    parser.add_argument('-a', action='store_true',
        help='show all files, including dotfiles.')
    parser.add_argument('-l',
        help='depth or level limit')
    return parser


'''
TODO: 
if Directory == None.
Save the data into a Dictionary of Dictionaries?
Figure out how to add the tree-like display with the pipes.
Gotta add permission errors. *sigh*
I've got pipes. How do I stop them?
I think creating a list of strings to use as the pipes might be the answer.
arr = [LINES, LINES, LINES, LINES]
If Last item in directory or len(items_in_folder - 1)
arr[n-1] = [SPACES]
Problem with that solution:
    the case where the inner directory finishes before the outer directories
        ├─ DIR:
        │  ├─ FILE:
        │  ├─ FILE:
        │  ├─ DIR:
        │  ├─ DIR:
        │  ├─ DIR:
        │  ├─ DIR:
        │  ├─ FILE:
        │  ├─ DIR:
        │  ├─ DIR:
        │  ├─ FILE:
        │  ├─ FILE:
        │  └─ FILE: <---- This will change arr[0] to SPACES
        ├─ DIR:
            └─ FILE: <---- Causing this mess
        ├─ FILE:
        └─ DIR:
            ├─ DIR: <--- These lines are correct though.
            ├─ DIR: <---    "   "     "     "       " 
            ├─ DIR: <---    "   "     "     "       " 
            └─ DIR: <---    "   "     "     "       " 
'''
def how_far(directory, hidden, limit=None, n=0, last_line=False):
    if n == 0:
        print(directory)
    if n == limit:
        return
    elif directory.is_dir():
        items_in_folder = [item for item in directory.iterdir()]
        for item in range(len(items_in_folder)):
            if last_line == True and n == 0:
                pass
            else:
                if (items_in_folder[item].name).startswith('.') and not hidden:
                    pass
                elif item == len(items_in_folder) - 1:
                    if items_in_folder[item].is_dir():
                        print('{}{} DIR:{}'.format(LINES*n, "└─", items_in_folder[item].name))
                        how_far(items_in_folder[item], hidden, limit, n+1, last_line=True)
                    
                    else:
                        print('{}{} FILE:{}'.format(LINES*n, "└─", items_in_folder[item].name))
                elif items_in_folder[item].is_dir():
                    print('{}{} DIR:{}'.format(LINES*n, "├─", items_in_folder[item].name))
                    how_far(items_in_folder[item], hidden, limit, n+1)
                    
                else:
                    print('{}{} FILE:{}'.format(LINES*n, "├─", items_in_folder[item].name))
    else:
        return None

def limit_or_none(directory, hidden, limit):
    if limit == None:
        how_far(directory, hidden)
    else:
        how_far(directory, hidden, int(limit))


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    p = pathlib.Path(args.directory)
    limit_or_none(p, args.a, args.l)
