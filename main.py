import asyncio

from constants import LINK_EXAMPLE
from examples import extract_by_aiohttp, extract_by_niquests, extrat_by_request


class Main:
    def __init__(self, request, aiohttp, niquests):
        self.request = request
        self.aiohttp = aiohttp
        self.niquests = niquests

    async def run(self):
        self.request(url=LINK_EXAMPLE, framework='requests')
        await self.aiohttp(url=LINK_EXAMPLE, framework='aiohttp')
        await self.niquests(url=LINK_EXAMPLE, framework='niquests')


if __name__ == "__main__":
    main = Main(extrat_by_request,extract_by_aiohttp,extract_by_niquests)
    for _ in range(10):
        asyncio.run(main.run())
