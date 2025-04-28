import asyncio
import time


async def calculate_sum(start: int, end: int) -> int:
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

async def main():
    N = 10_000_000_000_000
    num_tasks = 4
    chunk = N // num_tasks

    tasks = []
    for i in range(num_tasks):
        s = i * chunk + 1
        e = (i + 1) * chunk if i < num_tasks - 1 else N
        tasks.append(asyncio.create_task(calculate_sum(s, e)))

    partials = await asyncio.gather(*tasks)
    return sum(partials)

if __name__ == "__main__":
    t0 = time.perf_counter()
    total_sum = asyncio.run(main())
    t1 = time.perf_counter()
    print(f"Asyncio: sum = {total_sum}, time = {t1 - t0:.2f} s")
