from typing import Callable
from time import perf_counter
from csv import writer
from pathlib import Path


path = Path('benchmark.csv')

def benchmark(func: Callable) -> Callable:

    def inner(url, framework):
        writer_header = not path.exists()

        start = perf_counter()
        result = func(url, framework)
        end = perf_counter()

        execution_time = end - start

        with path.open('a', newline='') as csvfile:
            csvwriter = writer(csvfile)

            if writer_header:
                csvwriter.writerow(['name_framework','execution_time'])
            csvwriter.writerow([framework,execution_time])

        return result
    return inner
