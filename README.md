# oslo.concurrency.lab

A lab to play and test oslo.concurrency.


## Usage

Setup your lab:

```sh
# clone the lab locally (by example in ~/)
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
├── pocs
├── README.md
└── requirements.txt
```

The `pocs` directory store all the given available pocs that you can
use to emulate some classical use case of oslo.concurrency.

The `README.md` file (this file), give you some doc and example and help you
to use this lab.

The `requirements.txt` store all the default needed dependencies to play with
this lab. By default all the dependencies are pulled from pypi and official
repositories but in the case where you want to tests some development version
or things like that, then you need to delete the already installed requirements
that you want to test here and install your development version
from your local environment by example. See the fasteners example for more
related examples.

### fasteners locks by offset

Test fasteners locks managed by file offset.

The goal of this POC is to ensure that everything work fine
by introducing locks managed by file offset instead of creating
all file per lock like the current version of fasteners.

Setup fasteners:

```sh
$ pwd
~/oslo.concurrency.log
$ # be sure to use your virtualenv created previously
$ pipenv shell
$ # clone fasteners somewhere in your file system (by example in ~/)
$ git clone https://github.com/harlowja/fasteners
$ cd fasteners
$ git checkout offset-locks
$ pip uninstall fasteners
$ python setup.py develop
# Then return to your lab clone
$ cd ~/oslo.concurrency.lab
```

Also you need to setup oslo.concurrency to introduce some new params and
adapt the code:

```sh
$ pwd
~/oslo.concurrency.log
$ # be sure to use your virtualenv created previously
$ pipenv shell
$ # clone fasteners somewhere in your file system (by example in ~/)
$ git clone https://github.com/4383/oslo.concurrency -b debug-lockfile-delete
$ cd oslo.concurrency
$ pip uninstall oslo.concurrency
$ python setup.py develop
# Then return to your lab clone
$ cd ~/oslo.concurrency.lab
```

Then execute the poc:

```sh
$ # getting help
$ ./pocs/locks/poc.sh -h
$ # run all scenarios with the default config
$ ./pocs/locks/poc.sh
$ # run specific scenario
$ ./pocs/locks/poc.sh -s=scenario1
```

You can use the help or take a look to the script (`pocs/locks/poc.sh`)
to get different scenarios

Scenarios help you to test offset and mixed locks.

### reset your lab

```sh
$ cd <path to your clone of oslo.concurrency.lab>
$ deactivate
$ pipenv --rm
$ pipenv shell
$ pip install -r requirements
```
