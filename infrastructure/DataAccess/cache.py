import json
from fastapi.encoders import jsonable_encoder
import redis
from application.Contract.DataAccess.cache_interface import ICache


class Cache(ICache):
    def __init__(self, host, port, username, password, db=0):
        try:
            print(host, port, username, password, db)
            redis_client = redis.StrictRedis(
                host=host,
                port=port,
                username=username,
                password=password,
                db=db,
                decode_responses=True
            )
            redis_client.ping()
            self.redis_client = redis_client
        except Exception as e:
            print(f"Redis exception : ", e)
            self.redis_client = None
        
    async def set_item(self, key: str, value: object) -> None:
        print("Setting key", key, " value ", value)
        if self.redis_client is None:
            return None
        json_value = json.dumps(jsonable_encoder(value))
        self.redis_client.set(key, json_value)

    async def get_item(self, key: str) -> object | None:
        if self.redis_client is not None:
            value = self.redis_client.get(key)
            if value:
                return json.loads(value)
        return None