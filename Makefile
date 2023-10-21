setup:
	python -m venv ~/.capstone

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	hadolint Dockerfile
	pylint --disable=R,C,W1203,W1202,E0601,W0621 app.py