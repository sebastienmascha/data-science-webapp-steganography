
build:
	docker-compose build
up:
	docker-compose up -d

down:
	docker-compose down

restart:
	make build
	make down
	make up

deploy:
	docker-compose -f docker-compose.prod.yml build
	docker-compose -f docker-compose.prod.yml down
	docker-compose -f docker-compose.prod.yml up -d
