setup:
	python -m venv ~/.capstone

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	hadolint Dockerfile
	pylint --dasble=R,C,W1203,W1202 appy.py