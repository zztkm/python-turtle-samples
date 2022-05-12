import typer

from tutorial import tutorial

app = typer.Typer()


cmds = {
        "tutorial": tutorial
        }


@app.command()
def run(name: str):
    typer.secho(f"run {name}", fg=typer.colors.GREEN)
    func = cmds.get(name)
    if not func:
        typer.secho(f"{name} does not exist", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    func()
    input("Press Enter to Exit")


if __name__ == "__main__":
    app()
