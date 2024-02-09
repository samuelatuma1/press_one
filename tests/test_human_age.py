import pytest
from unittest.mock import Mock
from application.Features.human_age_feature import HumanAgeFeature
from domain.Responses.human_age_api_response import HumanAgeApiResponse
from application.Common.Exceptions.age_not_found_exception import AgeNotFoundException
from domain.Responses.human_age_response import HumanAgeResponse
from tests.Fakes.fake_age_api import FakeAgeApi, FakeAgeApiReturningNoneForGetAgeByName
from tests.Fakes.fake_cache import FakeHumanAgeCache, FakeHumanAgeCacheReturnsNoneForGetAgeByName


@pytest.mark.asyncio
async def test_human_age_feature_does_not_call_api_if_cache_returns_data():
    # Arrange
    mock_human_age_cache = FakeHumanAgeCache()
    
    mock_age_api =  FakeAgeApi()
    # Act
    human = HumanAgeFeature(mock_human_age_cache, mock_age_api)
    print("ha")
    print(human)
    returned_age = await human.get_human_age("test")
    print(returned_age)
    assert returned_age.age == 1
    # Assert


@pytest.mark.asyncio
async def test_human_age_feature_calls_api_if_cache_returns_none():
    # Arrange
    mock_human_age_cache = FakeHumanAgeCacheReturnsNoneForGetAgeByName()
    mock_age_api =  FakeAgeApi()
    human = HumanAgeFeature(mock_human_age_cache, mock_age_api)

    # Act
    returned_age = await human.get_human_age("test")

    # Assert
    assert returned_age.age == 2

@pytest.mark.asyncio
async def test_human_age_raises_AgeNotFoundException_if_age_for_name_not_found_in_cache_and_api():
    # Arrange
    mock_human_age_cache = FakeHumanAgeCacheReturnsNoneForGetAgeByName()
    mock_age_api =  FakeAgeApiReturningNoneForGetAgeByName()
    human = HumanAgeFeature(mock_human_age_cache, mock_age_api)

    # Assert
    with pytest.raises(AgeNotFoundException):
        await human.get_human_age("test")

@pytest.mark.asyncio
async def test_human_age_returns_HumanAgeResponse_If_Cache_Returns_With_Data():
    # Arrange
    mock_human_age_cache = FakeHumanAgeCache()
    mock_age_api =  FakeAgeApiReturningNoneForGetAgeByName()
    human = HumanAgeFeature(mock_human_age_cache, mock_age_api)

    # Act
    returned_age = await human.get_human_age("test")
    # Assert
    assert isinstance(returned_age, HumanAgeResponse)

@pytest.mark.asyncio
async def test_human_age_returns_HumanAgeResponse_If_Api_Returns_With_Data():
    # Arrange
    mock_human_age_cache = FakeHumanAgeCacheReturnsNoneForGetAgeByName()
    mock_age_api =  FakeAgeApi()
    human = HumanAgeFeature(mock_human_age_cache, mock_age_api)

    # Act
    returned_age = await human.get_human_age("test")
    # Assert
    assert isinstance(returned_age, HumanAgeResponse)

