# sam-fastapi-mangum-poc

PoC using AWS SAM, FastAPI, Mangum and Pydantic


## Prerequisites
* [Python 3.10](https://www.python.org/downloads/)
* [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Docker](https://hub.docker.com/search/?type=edition&offering=community)

## Quick start

1. Create a virtual environment and activate it:
```bash
python -m venv .venv && source .venv/bin/activate
```

2. Install the dependencies
```bash
make install
```

3. Running locally
```bash
make run
```

## Maintenance

```bash
make lint && make validate
```

## Build and Deploy
```bash
make build && make deploy

## Testing
```bash
make tests
```


## TODO
* [ ] Make tests work (unit and integration)
