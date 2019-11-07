import fcntl
import time

testfile = "/tmp/test-offset"
print("opening fd1")
fd1 = open(testfile, "w+")

fcntl.lockf(fd1, fcntl.LOCK_EX, 0, 1, 1)
print("fd1 pointer position: {}".format(fd1.tell()))
fd1.write("test fd 1\n")
print("fd1 pointer position: {}".format(fd1.tell()))

time.sleep(2)

print("opening fd2")
fd2 = open(testfile, "a+")
print("fd2 pointer position: {}".format(fd2.tell()))
print("changing fd2 pointer position")
fd1.seek(0, 0)
print("fd2 pointer position: {}".format(fd2.tell()))
fd2.write("test fd 2\n")
print("fd2 pointer position: {}".format(fd2.tell()))

time.sleep(2)
print("changing fd1 pointer position")
fd1.seek(0, 0)
print("fd1 pointer position: {}".format(fd1.tell()))
fd1.write("test fd 1 seeked\n")
fd1.close()
time.sleep(2)
fd2.close()
