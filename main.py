"""Example of using svcs with FastAPI."""
from __future__ import annotations

import os
from typing import AsyncGenerator

import svcs
from fastapi import FastAPI

# TODO: load multiple db_urls from env file via pydantic settings
config = {"db_url": os.environ.get("DB_URL", "sqlite:///:memory:")}


# TODO: when-tested: try: sqlite-utils connection
# TODO: when-tested: try: pypika for queries?
class Database:
    @classmethod
    async def connect(cls, db_url: str) -> Database:
        return Database()

    async def get_user(self, user_id: int) -> dict[str, str]:
        return {}  # not interesting here


# TODO: Use Annotations to provide multiple databases
# https://svcs.hynek.me/en/stable/core-concepts.html#multiple-factories-for-the-same-type

# TODO: when-tested: Move database connection to another module
# TODO: when-tested: Move service container setup to another module


@svcs.fastapi.lifespan
async def lifespan(app: FastAPI, registry: svcs.Registry) -> AsyncGenerator[dict[str, object], None]:
    async def connect_to_db() -> Database:
        # TODO: acquire settings from another service
        # https://svcs.hynek.me/en/stable/core-concepts.html#containers
        return await Database.connect(config["db_url"])

    registry.register_factory(Database, connect_to_db)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/users/{user_id}")
async def get_user(user_id: int, services: svcs.fastapi.DepContainer) -> dict:
    db = await services.aget(Database)

    # TODO: when-tested: try: move logic to another module and inject databases
    # TODO: when-tested: try: injecting whole service container instead

    try:
        return {"data": await db.get_user(user_id)}
    except Exception as e:
        return {"exception": e.args[0]}
