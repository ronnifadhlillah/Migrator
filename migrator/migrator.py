import click

@click.group()
def main():
    """MIGRATOR : THE DATABASE MADE IN CLI"""

@main.command()
@click.option('--db', nargs=1, type=str)
def init(db):
    click.echo("%s world" %db)
