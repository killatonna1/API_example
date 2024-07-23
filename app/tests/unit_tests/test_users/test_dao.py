



from httpx import AsyncClient
import pytest
from app.registration.dao import UsersDao

@pytest.mark.parametrize("id, exists", [
    (1, True),
    (2, True),
    (3, False),
])
async def test_find_user_by_id(id, exists, ac: AsyncClient):
    user = await UsersDao.find_by_id(id)
    
    if exists:
        assert user
        assert user.id == id
    else:
        print("User is not exists!")
    
    
    
    
