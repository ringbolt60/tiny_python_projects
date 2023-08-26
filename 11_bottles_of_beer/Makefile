.PHONY: test

test:
	pytest -xvv test.py

sums:
	./mk-sums.sh > sums.txt

build:
	chmod +x ./bottles.py
	cp ./bottles.py ~/bin
