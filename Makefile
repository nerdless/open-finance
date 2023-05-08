docker-build:
	docker build -t expense-tracker .

docker-run:
	docker run --rm -p 8000:8000 -v $(shell pwd)/src:/app expense-tracker

docker-stop:
	docker stop $(shell docker ps -aq --filter name=expense-tracker)