"""Command 2."""

import click


@click.command()
@click.option('--count', default=1, help='Loop count.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def main(count, name):
    """Run sample command.

    This is a sample command.
    """
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    main()
