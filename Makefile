.PHONY: tests

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install:
	pip install -r app/requirements.txt
	pip install -r requirements-dev.txt

tests:
	python -m pytest

lint:
	black .
	isort . --profile black

validate:
	sam validate --debug --lint

clean:
	rm -rf .aws-sam/

run:
	uvicorn app.app:app --reload

build:
	sam build --use-container --debug

deploy:
	sam deploy --stack-name sam-fastapi-mangum --config-file samconfig.toml --debug
