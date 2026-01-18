### Install

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

In `/soundcloud_cron`:

```
uv sync
```

### Run

In `/soundcloud_cron`:

```
uv run --env-file .env -- main.py 
```