import typer
import asyncio
from services.scanner import find_config, read_config
from services.sender import send_config

app = typer.Typer()

@app.command()
def push(app_name: str):
    path = find_config(app_name)
    if path:
        content = read_config(path)
        asyncio.run(send_config(app_name, content))
        typer.echo(f" ✔ {app_name} send success! Found in {path}")
    else:
        typer.echo(f" ✖ {app_name} not found!")


@app.command()
def pull(app_name: str):
    typer.echo(f" ⬇ Команда pull для {app_name} ще в розробці!")

if __name__ == "__main__":
    app()