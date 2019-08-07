import pathlib
import argparse

LINES = '│  '
SPACE = '   '
def create_parser():

    parser = argparse.ArgumentParser(
        description='A program to list all the files and directories ' +
                    'in the specified directory. If no directory is specified, ' +
                    'the current directory will be used.',
        prog='PROG')
    parser.add_argument('directory', metavar='/path/to/dir')
    parser.add_argument('-a', action='store_true')
    parser.add_argument('-d')
    return parser


'''
TODO: 
Save the data into a Dictionary of Dictionaries?
Figure out how to add the tree-like display with the pipes.
Gotta add permission errors. *sigh*
I've got pipes. How do I stop them?
'''
def how_far(directory, hidden, limit, n=0, last_line=False):
    if n == 0:
        print(directory)

    if n == limit:
        return
    elif directory.is_dir():
        items_in_folder = [item for item in directory.iterdir()]
        if last_line == True and n == 0:
            pass
        else:
            for item in range(len(items_in_folder)):
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

def no_limit_tree(directory, hidden, last_line=False, n=0, bypass=False):
    if directory.is_dir():
        items_in_folder = [item for item in directory.iterdir()]
        if last_line == True and n == 0:
            for item in range(len(items_in_folder)):
                if (items_in_folder[item].name).startswith('.') and not hidden:
                    pass
                elif item == len(items_in_folder) - 1:
                    if items_in_folder[item].is_dir():
                        print('{}{} DIR:{}'.format(SPACE*n, "└─", items_in_folder[item].name))
                        no_limit_tree(items_in_folder[item], hidden, last_line=True, n=n+1)
                    
                    else:
                        print('{}{} FILE:{}'.format(SPACE*n, "└─", items_in_folder[item].name))
                elif items_in_folder[item].is_dir():
                    print('{}{} DIR:{}'.format(SPACE*n, "├─", items_in_folder[item].name))
                    no_limit_tree(items_in_folder[item], hidden, n=n+1)
                    
                else:
                    print('{}{} FILE:{}'.format(SPACE*n, "├─", items_in_folder[item].name)) 
        else:
            for item in range(len(items_in_folder)):
                if (items_in_folder[item].name).startswith('.') and not hidden:
                    pass
                elif item == len(items_in_folder) - 1:
                    if items_in_folder[item].is_dir():
                        print('{}{} DIR:{}'.format(LINES*n, "└─", items_in_folder[item].name))
                        no_limit_tree(items_in_folder[item], hidden, last_line=True, n=n+1)
                    
                    else:
                        print('{}{} FILE:{}'.format(LINES*n, "└─", items_in_folder[item].name))
                elif items_in_folder[item].is_dir():
                    print('{}{} DIR:{}'.format(LINES*n, "├─", items_in_folder[item].name))
                    no_limit_tree(items_in_folder[item], hidden, n=n+1)
                    
                else:
                    print('{}{} FILE:{}'.format(LINES*n, "├─", items_in_folder[item].name))

def limit_or_none(directory, hidden, limit):
    if limit == None:
        no_limit_tree(directory, hidden)
    else:
        how_far(directory, hidden, int(limit))

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    p = pathlib.Path(args.directory)
    print(p)
    limit_or_none(p, args.a, args.d)