import asyncio
import os
import aiohttp

from gidgethub.aiohttp import GitHubAPI

async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "joker_bot", oauth_token=os.getenv("joker"))
        await gh.post("/repos/sohanjokerinfini/mayadata/pulls",
                      data={"title": "hello github bot  ",
                            "body" : "Thanks!"})

asyncio.run(main())