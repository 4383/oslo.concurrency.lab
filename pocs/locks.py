import argparse
import threading
import time

from oslo_concurrency import lockutils

import fasteners

OFFSET_SIZE = 2


@lockutils.synchronized('not_thread_safe_files', lock_file_prefix="foo",
        external=True, lock_path="/tmp")
def not_thread_safe_locked_with_oslo_concurrency_base(name, repeat, sleep):
    """using oslo.concurrency and fasteners lock files"""
    for el in range(repeat):
        print(name)
        time.sleep(2)


@lockutils.synchronized('not_thread_safe_offset', lock_file_prefix="bar",
        external=True, lock_path="/tmp", offset=OFFSET_SIZE)
def not_thread_safe_locked_with_oslo_concurrency_offset(name, repeat, sleep):
    """using oslo.concurrency and fasteners locks by offset"""
    for el in range(repeat):
        print(name)
        time.sleep(2)


@lockutils.synchronized('not_thread_safe_offset', lock_file_prefix="bar",
        external=True, lock_path="/tmp", offset=3)
def not_thread_safe_locked_with_oslo_concurrency_offset_parallel(name, repeat, sleep):
    """using oslo.concurrency and fasteners locks by offset"""
    for el in range(repeat):
        print(name)
        time.sleep(2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--offset', action="store_true")
    parser.add_argument('-t', '--threads', type=int, default=2)
    parser.add_argument('-r', '--repeat', type=int, default=5)
    parser.add_argument('-s', '--sleep', type=int, default=2)
    args = parser.parse_args()

    target = not_thread_safe_locked_with_oslo_concurrency_base
    parafunc = not_thread_safe_locked_with_oslo_concurrency_base
    if args.offset:
        target = not_thread_safe_locked_with_oslo_concurrency_offset
        parafunc = not_thread_safe_locked_with_oslo_concurrency_offset_parallel

    print("#" * (len(target.__doc__) + 4))
    print("  {}".format(target.__name__))
    print("  {}".format(target.__doc__))
    print("#" * (len(target.__doc__) + 4))

    threads = []
    for el in range(args.threads):
        passed_args = ("thread-{}".format(el), args.repeat, args.sleep)
        t = threading.Thread(target=target, args=passed_args)
        threads.append(t)

    parallel = threading.Thread(target=parafunc,
                                args=("parallel", args.repeat, args.sleep))
    threads.append(parallel)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    parallel.join()

    print("done")


if __name__ == "__main__":
    main()
