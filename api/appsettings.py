
from dotenv import load_dotenv
import os
from  application.Contract.Api.age_api_interface import IAgeApi
from  application.Contract.DataAccess.cache_interface import ICache
from  application.Contract.DataAccess.human_age_cache_interface import IHumanAgeCache
from  application.Contract.Features.human_age_feature_interface import IHumanAgeFeature
from  application.Features.human_age_feature import HumanAgeFeature
from  infrastructure.Api.age_api import AgeApi
from  infrastructure.DataAccess.cache import Cache
from  infrastructure.DataAccess.human_age_cache import HumanAgeCache

load_dotenv()  
cache : ICache | None = None

def cache_factory() ->ICache:
    global cache
    if cache is None:
        cache = Cache(
        os.getenv("redis_host"), 
        os.getenv("redis_port"), 
        os.getenv("redis_username"),
        os.getenv("redis_password"),
        os.getenv("redis_db"))
    return cache
    
def human_age_cache_factory()-> IHumanAgeCache:
    return HumanAgeCache(cache_factory())

def age_api_factory() -> IAgeApi:
    return AgeApi()

def human_age_feature() -> IHumanAgeFeature:
    return HumanAgeFeature(human_age_cache_factory(), age_api_factory())





