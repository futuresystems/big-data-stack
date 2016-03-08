UNAME := $(shell uname)

BROWSER=firefox
ifeq ($(UNAME), Darwin)
BROWSER=open
endif
ifeq ($(UNAME), Windows)
BROWSER=/cygdrive/c/Program\ Files\ \(x86\)/Google/Chrome/Application/chrome.exe
endif
ifeq ($(UNAME), CYGWIN_NT-6.3)
BROWSER=/cygdrive/c/Program\ Files\ \(x86\)/Google/Chrome/Application/chrome.exe
endif

doc: man
	sphinx-apidoc -f -o docs/source/code cloudmesh_client
	cd docs; make html
	cp -r scripts docs/build/html

d:
	rm -rf build
	pip uninstall -y cloudmesh_client
	pip uninstall -y cloudmesh_client
	python setup.py install; python cloudmesh_client/db/CloudmeshDatabase.py
	cm hpc run uname --cluster=india

db:
	rm ~/.cloudmesh/cloudmesh.db
	cm default list

test:
	echo $(UNAME)

publish:
	ghp-import -n -p docs/build/html

view:
	$(BROWSER) docs/build/html/index.html

man: cloudmesh
	cm man > docs/source/man/man.rst

# cm debug off')
# cm man | grep -A10000 \"Commands\"  | sed \$d  > docs/source/man/man.rst

cloudmesh:
	python setup.py install

setup:
	python setup.py install

dist: clean setup
	python setup.py sdist --formats=gztar,zip
	python setup.py bdist
	python setup.py bdist_wheel

upload_test:
	python setup.py  sdist bdist bdist_wheel upload -r https://testpypi.python.org/pypi

upload:
	python setup.py  sdist bdist bdist_wheel upload -r https://pypi.python.org/pypi

log:
	gitchangelog | fgrep -v ":dev:" | fgrep -v ":new:" > ChangeLog
	git commit -m "chg: dev: Update ChangeLog" ChangeLog
	git push

######################################################################
# TESTING
######################################################################

pytest:
	make -f Makefile clean
	pip install -r requirements.txt
	python setup.py install
	cm register remote
	py.test tests

nosetest:
	make -f Makefile clean
	pip install -r requirements.txt
	python setup.py install
	cm register remote
	nosetests -v --nocapture tests

######################################################################
# CLEANING
######################################################################

clean:
	rm -rf *.zip
	rm -rf *.egg-info
	rm -rf *.eggs
	rm -rf docs/build
	rm -rf build
	rm -rf dist
	find . -name '__pycache__' -delete
	find . -name '*.pyc' -delete
	-pip uninstall cloudmesh_client -y
	rm -rf .tox

######################################################################
# TAGGING
######################################################################

tag:
	bin/new_version.sh

rmtag:
	python setup.py rmtag

######################################################################
# DOCKER
######################################################################

docker-mahine:
	docker-machine create --driver virtualbox cloudmesh

docker-machine-login:
	eval "$(docker-machine env cloudmesh)"

docker-build:
	docker build -t laszewski/cloudmesh .

# dockerhub
docker-login:
	docker login

docker-push:
	docker push laszewski/cloudmesh

docker-pull:
	docker pull laszewski/client

#
# does not work yet
#
docker-run:
	docker run -t -i cloudmesh /bin/bash

docker-clean-images:
	bin/docker-clean-images

