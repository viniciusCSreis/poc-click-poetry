import click
from random_cli_framework.logic import sum_of_xy


@click.Group
def cli():
    pass


@cli.command()
def hello():
    print("sum:", sum_of_xy(10, 1))


def main():
    cli()


if __name__ == '__main__':
    main()
