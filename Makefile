ifeq (,$(shell which docker-compose))
HAS_DOCKER_COMPOSE=False
else
HAS_DOCKER_COMPOSE=True
endif

build_airflow:
ifeq (True,$(HAS_DOCKER_COMPOSE))
	docker-compose -f airflow/docker-compose.yaml up --build -d --remove-orphans
endif

build_datawarehouse:
ifeq (True,$(HAS_DOCKER_COMPOSE))
	docker-compose -f postgres/docker-compose.yaml up --build -d --remove-orphans
endif

build_app:
ifeq (True,$(HAS_DOCKER_COMPOSE))
	docker-compose -f app/docker-compose.yaml up --build -d --remove-orphans
endif

down_airflow:
	docker-compose -f airflow/docker-compose.yaml down

