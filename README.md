# sam-fastapi-mangum-poc
PoC using AWS SAM, FastAPI, Mangum, and Pydantic.

The benefit is that we use FastAPI to generate our OpenAPI documentation and integrate it with API Gateway.


## Prerequisites
* [Python 3.10](https://www.python.org/downloads/)
* [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Docker](https://hub.docker.com/search/?type=edition&offering=community)


## Quick start
1. Create a [virtual environment](https://docs.python.org/3.10/library/venv.html) and activate it
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
> http://127.0.0.1:8080/docs

## Build and Deploy
1. Building
```bash
make build
```
2. Deploy
```bash
make deploy
```

## Testing
```bash
make tests
```

## Maintenance
```bash
make lint && make validate
```

> For useful commands, run: `make help`


## TODO
* [ ] Make tests work (unit and integration)
