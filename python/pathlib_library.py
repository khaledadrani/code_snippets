#source: https://realpython.com/python-pathlib/ 
import pathlib

#print current work directory
pathlib.Path.cwd()

#instanciate windows path: 
pathlib.Path(r'C:\Users\khale')

# forward slash operator 
pathlib.Path.home() / 'python' / 'scripts' / 'test.py'
pathlib.Path.home().joinpath('python', 'scripts', 'test.py')

# reading and writing files
path = pathlib.Path.cwd() / 'test.md'
with open(path, mode='r') as fid:
    headers = [line.strip() for line in fid if line.startswith('#')]
print('\n'.join(headers))

#read file as text string
path.read_text()

#read file as bytes (additional characters like escape)
path.read_bytes()


#read file as text string 
path.write_text()

#read file as bytes (additional characters like escape)
path.write_bytes()

#find full path
path.resolve()

#path components: get parent of current path
path.parent

#path components: get name of current path
path.name

#path components: the file name without the suffix
path.stem

#path components: the file extension
path.suffix

#path components: maybe drive or volume (part before directories)
path.anchor

#moving and deleting files
if not destination.exists():
    source.replace(destination)

with destination.open(mode='xb') as fid:
    fid.write(source.read_bytes())

#iterate over files in directory
path.iterdir()

#Counting Files
import collections
collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir())

#search with patterns: glob and rglob (recursive)
path.glob("*.p")
path.rglob("*.py")

# display a directory tree
def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')

# Find the Last Modified File
from datetime import datetime
time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
print(datetime.fromtimestamp(time), file_path)

# Create a Unique Numbered File Name
def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path

path = unique_path(pathlib.Path.cwd(), 'test{:03d}.txt')
