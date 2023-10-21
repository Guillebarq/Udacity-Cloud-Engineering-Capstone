setup:
	python -m venv ~/.capstone

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	wget -O ./hadolint https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64 &&\
		chmod +x ./hadolint

lint:
	./hadolint Dockerfile
	pylint --disable=R,C,W1203,W1202,E0601,W0621 app.py

all: install lint