create:
	python3 -m venv env

activate:
	source env/bin/activate

install:
	pip3 install -r requirements.txt

freeze:
	pip3 freeze > requirements.txt

test:
	python3 -m unittest discover
	
