import requests

from wrapper import benchmark

@benchmark
def run_requests(url, framework):
    return requests.get(url, framework)
