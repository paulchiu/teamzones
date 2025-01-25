# Teamzones

Given a set of time zones and a time, print the time in different timezones.

## Usage

```shell
tz at [CSV of time zones] [time to get]
```

Example

```shell
❯ tz at 'Australia/Melbourne,Australia/Brisbane' 3pm
04:00PM AEDT / 03:00PM AEST
```

To find the list of valid time zones, run the command

```shell
tz list-countries
```

## Development

### Set up

To install dependencies, do

```shell
poetry install --no-root
```

### Dev loop

```shell
poetry sync
python teamzones
```

### Install loop

```shell
poetry install
tz --help
```
