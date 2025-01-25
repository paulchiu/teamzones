import typer
from zoneinfo import ZoneInfo, available_timezones
from dateutil import parser
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def at(timezones: str, time: Annotated[Optional[str], typer.Argument()] = None):
    # Convert timezones to ZoneInfo
    timezones_list = timezones.split(",")
    zone_infos = list(map((lambda tz: ZoneInfo(tz)), timezones_list))

    # Get user input time
    given_time = datetime.now() if time == None else parser.parse(time)

    # Get output timezones
    zoned_times = list(map((lambda zi: given_time.astimezone(zi)), zone_infos))
    time_format = "%I:%M%p %Z"
    formatted_times = list(map((lambda t: t.strftime(time_format)), zoned_times))
    typer.echo(" / ".join(formatted_times))


@app.command()
def list_countries():
    timezones = sorted(available_timezones())
    for timezone in timezones:
        print(timezone)


if __name__ == "__main__":
    app()
