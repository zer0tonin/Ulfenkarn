# -*- mode: makefile -*-

COMPOSE = docker-compose -p ulfenkarn


.PHONY: run
run:
	$(COMPOSE) build ulfenkarn
	$(COMPOSE) run ulfenkarn

.PHONY: down
down:
	$(COMPOSE) down --volumes --rmi=local


.PHONY: format
format:
	black --target-version py37 ulfenkarn


.PHONY: style
style:
	black --target-version py37 --check ulfenkarn


.PHONY: complexity
complexity:
	xenon --ignore "tests" --max-absolute A --max-modules A --max-average A ulfenkarn


.PHONY: test
test:
	pytest -s ulfenkarn


.PHONY: security-sast
security-sast:
	bandit -r ulfenkarn -x test


.PHONY: type
type:
	mypy ulfenkarn --ignore-missing-import
