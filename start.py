import argparse

from binary_practice import start_cli, start_gui

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cli', action='store_true', 
        help='Open with CLI')
    args = parser.parse_args()
    if args.cli:
        start_cli()
    else:
        start_gui()
