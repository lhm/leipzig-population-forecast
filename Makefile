data/population-forecast.csv: venv
	./venv/bin/python scripts/population-forecast.py

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*.csv
	rm -rf pdfs/*.pdf

clean-venv:
	rm -rf venv

.PHONY: clean clean-venv