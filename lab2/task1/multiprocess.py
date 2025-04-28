import multiprocessing as mp
import time


def calculate_sum(start: int, end: int) -> int:
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

def worker(args):
    return calculate_sum(*args)

if __name__ == "__main__":
    N = 10_000_000_000_000
    num_procs = mp.cpu_count()
    chunk = N // num_procs

    args_list = []
    for i in range(num_procs):
        s = i * chunk + 1
        e = (i + 1) * chunk if i < num_procs - 1 else N
        args_list.append((s, e))

    t0 = time.perf_counter()
    with mp.Pool(processes=num_procs) as pool:
        results = pool.map(worker, args_list)
    total_sum = sum(results)
    t1 = time.perf_counter()

    print(f"Multiprocessing: sum = {total_sum}, time = {t1 - t0:.2f} s")
