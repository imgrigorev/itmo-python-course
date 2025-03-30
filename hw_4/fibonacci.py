import time
from threading import Thread
from multiprocessing import Process


def fibo_time(n, type_=None):
    start = time.time()
    a, b = 1, 0
    for _ in range(n - 1):
        a, b = a + b, a
    with open("hw_4/artifacts/artifacts_fibo.txt", "a", encoding="utf-8") as file:
        if not type_:
            file.write(f"Synchronous {time.time() - start:.4f}s\n")
        elif type_ == "thread":
            file.write(f"Thread {time.time() - start:.4f}s\n")
        elif type_ == "process":
            file.write(f"Process {time.time() - start:.4f}s\n")
        else:
            raise ValueError("Unknown type")


open("hw_4/artifacts/artifacts_fibo.txt", "w").close()

start_group = time.time()

for i in range(10):
    fibo_time(100000)

with open("hw_4/artifacts/artifacts_fibo.txt", "a", encoding="utf-8") as file:
    file.write(f"\nSynchronous total time is {time.time() - start_group:.4f}s\n\n")

start_group = time.time()

threads = []
for _ in range(10):
    t = Thread(target=fibo_time, args=(100000, "thread"))
    t.start()
    threads.append(t)
for t in threads:
    t.join()

with open("hw_4/artifacts/artifacts_fibo.txt", "a", encoding="utf-8") as file:
    file.write(f"\nThread total time is {time.time() - start_group:.4f}s\n\n")

start_group = time.time()

processes = []
for _ in range(10):
    p = Process(target=fibo_time, args=(100000, "process"))
    p.start()
    processes.append(p)
for p in processes:
    p.join()

with open("hw_4/artifacts/artifacts_fibo.txt", "a", encoding="utf-8") as file:
    file.write(f"\nProcess total time is {time.time() - start_group:.4f}s\n\n")
