init:
	pip install -r requirements.txt
lint:
	pep8 .
lint-disp:
	autopep8 -r -d .
lint-fix:
	autopep8 -i -r -a .
header:
	python scripts/add_headers.py
clean:
	rm -r *.pyc
zip:
	python scripts/zip.py
