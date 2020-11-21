import click
from . import db

@click.group()
def clia_main():
    pass

@clia_main.command()
@click.argument(
    "type-activity",
    type=click.Choice(["task", "project"], case_sensitive=False)
)
@click.option(
    "-n", "--name", 
    prompt="Name of the activity or project",
    help="The name of the activity."
)
def start(type_activity, name):
    """Start operations on tasks and projects."""
    click.echo(type_activity)
    click.echo(name)
    pass