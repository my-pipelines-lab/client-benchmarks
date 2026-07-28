import niquests

from examples.aiohttp import benchmark


@benchmark
async def extract_by_niquests(url, framework):
    return niquests.get(url)
