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

This lab is composed of few elements and concepts. The project tree
represent them:

```sh
$ tree -L 1
.
├── payloads
├── pocs
├── README.md
└── requirements.txt
```

The `payloads` directory help you to store the things to test against
oslo.concurrency, by example a new feature in a given library.

The `pocs` directory store all the given available pocs that you can
use to emulate some classical use case of oslo.concurrency.

The `README.md` file (this file), give you some doc and example and help you
to use this lab.

The `requirements.txt` store all the default needed dependencies to play with
this lab. By default all the dependencies are pulled from pypi and official
repositories but in the case where you want to tests some development version
or things like that, then you need to delete put your development version
in `payloads` and then with `pip` uninstall the default version and replace
it by the version in available in `payload`. See the fasteners example for more
related examples.

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
