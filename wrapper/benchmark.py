import inspect
from csv import writer
from pathlib import Path
from time import perf_counter

path = Path('benchmark.csv')

def benchmark(func):

    if inspect.iscoroutinefunction(func):
        async def async_wrapper(url, framework):
            writer_header = not path.exists()

            start = perf_counter()
            result = await func(url, framework)
            end = perf_counter()

            execution_time = (end - start)

            with path.open('a', newline='') as csvfile:  # noqa: ASYNC230
                csvwriter = writer(csvfile)

                if writer_header:
                    csvwriter.writerow(['name_framework','execution_time'])
                csvwriter.writerow([framework,execution_time])

            return result
        return async_wrapper

    def sync_wrapper(url, framework):
        writer_header = not path.exists()
        start = perf_counter()
        result = func(url, framework)
        end = perf_counter()

        execution_time = (end - start)

        with path.open('a', newline='') as csvfile:
            csvwriter = writer(csvfile)

            if writer_header:
                csvwriter.writerow(['name_framework','execution_time'])
            csvwriter.writerow([framework,execution_time])

        return result
    return sync_wrapper
