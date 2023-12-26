.PHONY: setup up d b ps node

build:
	docker compose build

setup:
	@make up
	@make ps
d:
	docker compose down
stop:
	docker compose stop

up:
	docker compose up -d
ps:
	docker compose ps

run:
	docker-compose exec app python main.py