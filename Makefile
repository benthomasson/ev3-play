
.PHONY: deploy

deploy:
	scp -p *.py robot@beeboo:
	scp -p *.py robot@jake:
	scp -p *.py robot@marceline:

