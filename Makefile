start:
	docker-compose pull
	docker-compose up -d backend
	echo  "\n\n  NOW ENTER:\njupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888\n\n"
	docker-compose exec backend bash
	

stop:
	docker-compose down

build:
	docker-compose build backend

up:
	docker-compose up -d backend 

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
