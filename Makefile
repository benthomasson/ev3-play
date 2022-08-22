
.PHONY: deploy chmod

chmod:
	chmod +x *.py

deploy: chmod
	scp -p *.py robot@beeboo:
	#scp -p *.py robot@jake:
	scp -p *.py robot@marceline:

