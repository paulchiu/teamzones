import typer
from zoneinfo import ZoneInfo, available_timezones

app = typer.Typer()

@app.command()
def main(name: str):
    typer.echo(f"Hello {name}!")

@app.command()
def list_countries():
    timezones = sorted(available_timezones())
    for timezone in timezones:
        print(timezone)

if __name__ == "__main__":
    typer.run(main)