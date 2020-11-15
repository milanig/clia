import click

@click.command()
@click.option(
    "--count", 
    default=1,
    help="Number of greetings."
)
@click.option(
    "--name", 
    prompt="Your name",
    help="The person to greet."
)
def clia_main(count, name):
    """Command Line Interface Assistant."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)