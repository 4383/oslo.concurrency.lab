import threading
import time
from oslo_concurrency import lockutils


@lockutils.synchronized('not_thread_safe')
def not_thread_safe(name, repeat):
    for el in range(repeat):
        print(name)
        time.sleep(2)


t1 = threading.Thread(target=not_thread_safe, args=("one", 1000))
t2 = threading.Thread(target=not_thread_safe, args=("two", 1000))

t1.start()
t2.start()
t1.join()
t2.join()

print("done")
