import requests

from wrapper import benchmark


@benchmark
def extrat_by_request(url, framework):
    return requests.get(url)
