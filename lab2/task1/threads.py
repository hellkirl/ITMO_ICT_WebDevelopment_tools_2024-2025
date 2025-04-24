import threading
import time

class SumThread(threading.Thread):
    def __init__(self, numbers: list[int]):
        super().__init__()
        self.numbers = numbers
        self.result = 0

    def run(self):
        self.result = sum(self.numbers)

def calculate_sum(data: list[int], num_threads: int) -> int:
    chunk_size = len(data) // num_threads
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i+1) * chunk_size if i < num_threads - 1 else len(data)
        thread = SumThread(data[start:end])
        threads.append(thread)
        thread.start()
    
    total = 0
    for thread in threads:
        thread.join()
        total += thread.result
    return total

if __name__ == "__main__":
    data = list(range(1, 10_000_000_000_000))
    num_threads = 4
    start_time = time.perf_counter()
    total = calculate_sum(data, num_threads)
    end_time = time.perf_counter()
    print(f"Threading -> Sum: {total} in {end_time - start_time:.4f} seconds")
