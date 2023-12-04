from pathlib import Path


def get_input(day, as_list=True):
    input_dir = Path('./data')
    input_dir.mkdir(exist_ok=True)

    filepath = input_dir / f'{day}.txt'

    with open(filepath) as f:
        if as_list:
            return f.read().splitlines()
        else:
            return f.read().strip()