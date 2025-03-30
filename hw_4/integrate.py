from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import math
import os


def integrate_range(f, a, b, n_iter):
    step = (b - a) / n_iter
    acc = 0
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10_000_000, executor_class=ProcessPoolExecutor):
    step = (b - a) / n_jobs
    chunk_iter = n_iter // n_jobs

    args = [(f, a + i * step, a + (i + 1) * step, chunk_iter) for i in range(n_jobs)]

    with executor_class(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate_range, *arg) for arg in args]
        results = [f.result() for f in futures]

    return sum(results)


cpu_num = os.cpu_count()

for i in range(1, cpu_num ** 2 + 1):
    with open("hw_4/artifacts/artifacts_integrate.txt", "a", encoding="utf-8") as file:
        start = time.time()
        result = integrate(math.cos, 0, math.pi / 2, n_jobs=i, executor_class=ThreadPoolExecutor)
        file.write(f"ThreadPoolExecutor with n_jobs {i}.\nIntegrate time is {time.time() - start:.4f}s\n")

with open("hw_4/artifacts/artifacts_integrate.txt", "a", encoding="utf-8") as file:
    file.write("\n")

for i in range(1, cpu_num ** 2 + 1):
    with open("hw_4/artifacts/artifacts_integrate.txt", "a", encoding="utf-8") as file:
        start = time.time()
        result = integrate(math.cos, 0, math.pi / 2, n_jobs=i, executor_class=ProcessPoolExecutor)
        file.write(f"ProcessPoolExecutor with n_jobs {i}.\nIntegrate time is {time.time() - start:.4f}s\n")
