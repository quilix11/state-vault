import typer
import asyncio
from services.scanner import find_config, read_config
from services.sender import send_config
from services.recipient import get_config

app = typer.Typer()

@app.command()
def push(config_name: str):
    path = find_config(config_name)
    if path:
        content = read_config(path)
        asyncio.run(send_config(config_name, content))
        typer.echo(f" ✔ {config_name} send success! Found in {path}")
    else:
        typer.echo(f" ✖ {config_name} not found!")


@app.command()
def pull(config_name: str):
    path = find_config(config_name)
    if not path:
        typer.echo(f" ✖ {config_name} not found!")
        return 
    data = asyncio.run(get_config(config_name))
    if data == "error":
        typer.echo(" ✖ Sorry but server not unavailable")

    elif data:
        w_data= data["content"]
        path.write_text(w_data)
        typer.echo(f" ✔ {config_name} write")


        

    
    

if __name__ == "__main__":
    app()