import os
import click

@click.command()
@click.option('--year', type=int)
@click.option('--day', type=int)
@click.option('--language', type=str, default='python')
def main(year, day, language):
    basedir = '/home/ramain/packages/AdventOfCode/'
    codedir = f'{year}/{day:02}'
    os.chdir(basedir)

    if not os.path.exists(codedir):
        os.system(f'mkdir {codedir}')

    os.chdir(codedir)
    if not os.path.isfile("input.txt"):
        os.system(f'aocd {year} {day} > input.txt')

    if language == 'python':
        template = 'main.py'
    elif language == 'rust':
        template = 'main.rs'
    else:
        raise NotImplementedError(f'Only python and rust templates so far,')
    if not os.path.isfile(template):
        os.system(f'cp {basedir}/templates/{template} ./')

if __name__ == '__main__':
    main()

