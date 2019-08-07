# Rypytree
## A pseudo implementation of the tree command in linux
### How to use
```
usage: rypytree.py [-h] [-a] [-l L] /path/to/dir

a program to list all the files and directories in the specified directory. If
no directory is specified, the current directory will be used.

positional arguments:
  /path/to/dir

optional arguments:
  -h, --help    show this help message and exit
  -a            show all files, including dotfiles.
  -l L          depth or level limit
```

### Things that need to be completed:
- PermissionErrors
- Clean up the pipes
- Refactor code to look cleaner
- allow for pattern input
- Full prefix argument
- Maybe transition to os instead of using pathlib
