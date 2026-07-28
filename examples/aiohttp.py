import aiohttp

from wrapper import benchmark


@benchmark
async def extract_by_aiohttp(link, framework):
    async with aiohttp.ClientSession() as session: # type: ignore  # noqa: SIM117
        async with session.get(link) as response:
            return response

