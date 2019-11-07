import argparse
import threading
import time
import os

import fasteners


def test_lock(name, offset=None, repeat=10):
    """Test lock"""
    for i in range(repeat):
        with fasteners.InterProcessLock('/tmp/tmp_lock_file', offset=offset):
            print('Process {name}: I have the lock'.format(name=name))
            time.sleep(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default=str(os.getpid()))
    parser.add_argument('-o', '--offset', type=int, default=0)
    parser.add_argument('-r', '--repeat', type=int, default=10)
    args = parser.parse_args()

    if args.offset:
        typeof = "Using offset: {}".format(args.offset)
    else:
        typeof = "No offset define, using simple lock file with this process"
    print("- New process: {} - {}".format(args.name, typeof))
    time.sleep(2)

    test_lock(args.name, args.offset, repeat=args.repeat)


if __name__ == "__main__":
    main()
