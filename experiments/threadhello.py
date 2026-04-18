from threading import Thread
from time import time, sleep


def sayhello(name):
    print(f"Hello {name}!")
    sleep(2)


threadlist = []
for name in ('Ana', 'Bella', 'Marius'):
    t = Thread(target=sayhello, args=(name,))
    threadlist.append(t)

starttime = time()
for thread in threadlist:
    thread.start()
    thread.join()

endtime = time() - starttime
print(f'Took {endtime}')
