install:
	pip install -r requirements.txt

test:
	FL_CONFIG=funkenlights/test/test.json nosetests funkenlights/test/