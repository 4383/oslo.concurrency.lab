import argparse
import threading
import time
import os

import fasteners


@fasteners.interprocess_locked('/tmp/tmp_lock_file')
def test_without_offset(name):
    """Without offset"""
    for i in range(10):
        print('Process {name}: I have the lock ({desc})'.format(
            name=name, desc=test_without_offset.__doc__))
        time.sleep(1)


@fasteners.interprocess_locked('/tmp/tmp_lock_file', offset=1)
def test_with_offset(name):
    """With offset"""
    for i in range(10):
        print('Process {name}: I have the lock ({desc})'.format(
            name=name, desc=test_with_offset.__doc__))
        time.sleep(1)


@fasteners.interprocess_locked('/tmp/tmp_lock_file', offset=2)
def test_with_different_offset(name):
    """With different offset"""
    for i in range(10):
        print('Process {name}: I have the lock ({desc})'.format(
            name=name, desc=test_with_different_offset.__doc__))
        time.sleep(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default=str(os.getpid()))
    parser.add_argument('-o', '--offset', action="store_true")
    parser.add_argument('-d', '--diff-offset', action="store_true")
    parser.add_argument('-t', '--threads', type=int, default=2)
    parser.add_argument('-r', '--repeat', type=int, default=5)
    parser.add_argument('-s', '--sleep', type=int, default=2)
    args = parser.parse_args()

    target = test_without_offset
    if args.offset:
        target = test_with_offset
    if args.diff_offset:
        target = test_with_different_offset

    print("#" * (len(target.__doc__) + 4))
    print("  New process: {}".format(args.name))
    print("  {}".format(target.__name__))
    print("  {}".format(target.__doc__))
    print("#" * (len(target.__doc__) + 4))

    target(args.name)


if __name__ == "__main__":
    main()
