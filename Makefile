install:
	pip install -r requirements.txt

run:
	python main.py
test:
	FL_CONFIG=funkenlights/test/test.json pytest -s funkenlights/test/

cover:
	FL_CONFIG=funkenlights/test/test.json pytest --cov=funkenlights --cov-report html funkenlights/test/