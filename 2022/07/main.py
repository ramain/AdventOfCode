
f = open('input', 'r')

dirs = []
files = []
filesizes = []
dirs.append('/')

dir_fs = []
dir_files = []

for line in f:
    line = line.split()
    if line[0].isdigit():
        dir_fs.append(int(line[0]))
        dir_files.append(line[1])

    if line[1] == 'cd':
        files.append(dir_files)
        filesizes.append(dir_fs)
        dir = line[2]
        dirs.append(dir)


print(dirs)