.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: init
init:
	pip install -U pip
	pip install pip-tools

.PHONY: reqs
reqs:
	pip-compile
	pip install -r requirements.txt

.PHONY: run
run:
	flask --app inventory --debug run

.PHONY: init_db
init_db:
	flask --app inventory --debug init_db

.PHONY: start_http
start_httpd:
	sudo nginx

.PHONY: stop_httpd
stop_httpd:
	sudo nginx -s stop

