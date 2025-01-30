# Teamzones Usage Examples

## Basic Usage

Get current time in multiple timezones:

```shell
❯ tz at 'Australia/Melbourne,America/New_York'
3pm AEDT / 11pm EST
```

Get specific time in multiple timezones:

```shell
❯ tz at 'Australia/Melbourne,America/New_York' 9am
9am AEDT / 5pm EST
```

## Formatting Options

Use 24-hour format:

```shell
❯ tz at --time-format='%H:%M %Z' 'Australia/Melbourne,America/New_York' 
15:00 AEDT / 23:00 EST
```

Custom separator:

```shell
❯ tz at --separator=' | ' 'Australia/Melbourne,America/New_York'
3pm AEDT | 11pm EST
```

Combined options:

```shell
❯ tz at --time-format='%H:%M %Z' --separator=' → ' 'Australia/Melbourne,America/New_York,Europe/London'
15:00 AEDT → 23:00 EST → 04:00 GMT
```

## Finding Available Timezones

List all available timezones:

```shell
tz list-timezones
```

This will show all valid timezone names you can use with the tool.
