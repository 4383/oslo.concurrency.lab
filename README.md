# oslo.concurrency.lab

A lab to play and test oslo.concurrency.


## Usage

Setup your lab:

```sh
$ git clone https://github.com/4383/oslo.concurrency.lab
$ cd oslo.concurrency.lab
$ pipenv shell
$ pip install -r requirements
```

### fasteners locks by offset

Test fasteners locks managed by file offset.

The goal of this POC is to ensure that everything work fine
by introducing locks managed by file offset instead of creating
all file per lock like the current version of fasteners.

Setup fasteners:

```sh
$ # use the `payloads` directory to clone the dependencies to test
$ cd payloads/
$ git clone https://github.com/harlowja/fasteners
$ cd fasteners
$ git checkout offset-locks
$ pip uninstall fasteners
$ python setup.py develop
$ cd ..
```

Then execute the poc:

```sh
$ python pocs/locks.py
```

### reset your lab

```sh
$ deactivate
$ pipenv --rm
$ rm -rf payloads/*
$ pipenv shell
$ pip install -r requirements
```
