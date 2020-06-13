"""Command 4."""

import sys

import click
from loguru import logger


def filter_stdout_logging(record):
    return record['level'].name in ['INFO', 'SUCCESS', 'WARNING']

def filter_stdout_verbose(record):
    return record['level'].name in ['DEBUG', 'INFO', 'SUCCESS', 'WARNING']


@click.group()
@click.option('--verbose', is_flag=True, help='Verbose mode(output debug log).')
def main(verbose):
    """Run sample command.

    This is a sample command.
    """
    logger.remove()
    if verbose:
        logger.add(sys.stdout, filter=filter_stdout_verbose)
    else:
        logger.add(sys.stdout, filter=filter_stdout_logging)
    logger.add(sys.stderr, level='ERROR')
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')
    try:
        1/0
    except ZeroDivisionError:
        logger.exception('exception.')
    logger.success('success')
    logger.trace('trace')

@main.command()
def sub1():
    """Run sub command 1."""
    logger.info('Sub command 1.')

@main.command()
def sub2():
    """Run sub command 2."""
    logger.info('Sub command  2.')


if __name__ == '__main__':
    main()
