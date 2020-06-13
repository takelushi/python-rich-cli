"""Command 3."""

import click

from app_name.command.command3.command import sub1
from app_name.command.command3.command import sub2

commands = {
    'sub1': sub1.main,
    'sub2': sub2.main
}


@click.group()
def main():
    """Run sample command.

    This is a sample command.
    """
    pass

for k, v in commands.items():
    main.add_command(v, name=k)


if __name__ == '__main__':
    main()
