import os


def separate():
    filenames = filter(lambda s: not s.startswith('_'), os.listdir('out'))

    for filename in filenames:
        basename = '-'.join(filename.split('-')[:-1])
        try:
            os.mkdir(f'out/{basename}')
        except FileExistsError:
            pass
        os.rename(f'out/{filename}', f'out/{basename}/{filename}')


if __name__ == '__main__':
    separate()
