
from httpx import AsyncClient
import pytest

@pytest.mark.parametrize("email,password,status_code",[
    ("qwe@lylala.com", "123qweqwr", 200),
    ("qwe@lylala.com", "123qweqwr", 409),
    ("asdsaf", "qgweewg", 422)
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "email": email,
        "password": password,
    })
    assert response.status_code == status_code
    
    
@pytest.mark.parametrize("email, password, status_code", [
    ("ya@loh.com", "oioioi", 200),
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/login",json={
        "email": email,
        "password": password,
    })
    assert response.status_code == status_code