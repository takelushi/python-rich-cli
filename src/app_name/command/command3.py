"""Command 3."""

import click


@click.group()
def main():
    """Run sample command.

    This is a sample command.
    """
    pass

@main.command()
def sub1():
    """Run sub command 1."""
    click.echo('Sub command 1.')

@main.command()
def sub2():
    """Run sub command 2."""
    click.echo('Sub command  2.')


if __name__ == '__main__':
    main()
