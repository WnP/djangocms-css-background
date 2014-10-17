all:
	python2 setup.py sdist

clean:
	rm -rf venv dist *.egg-info

deploy:
	twine upload dist/*
