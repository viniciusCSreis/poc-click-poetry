install:
	cd random-cli; make install

test: install
	cd random-cli-framework; make test
	cd random-cli; make test

bin:
	cd random-cli; make bin