from fastapi import APIRouter, Depends, Response, status, BackgroundTasks
from pydantic import TypeAdapter

from app.exceptions import IncorrectUsernameOrPassword, UserAlredyExistsException
from app.registration.dao import UsersDao
from app.registration.dependencies import get_current_user
from app.registration.models import Users
from app.registration.schemas import SUsers
from app.registration.dao import BaseDao

from app.registration.auth import authenticate_user, create_access_token, get_password_hash, verify_password
from app.tasks.tasks import send_comfirmation_email


# router = APIRouter(
#     prefix="/registration",
#     tags=["Registration"],
# )

# @router.get("")
# async def get_coords() -> SRegistration:
#     return await RegistrationDao.find_one_or_none("qwerty1234")
# # @router.get("/{unique_id}")
# # def get_coords(unique_id):
# #     pass

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)



@router.post("/register")
async def register_user(
    background_tasks: BackgroundTasks,
    user_data: SUsers):
    existing_user =  await UsersDao.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlredyExistsException
    hashed_password = get_password_hash(user_data.password)
    user = await UsersDao.add_registration(email = user_data.email,
                                   password = hashed_password,
                                   )
    type_adapter = TypeAdapter(SUsers)
    user_dict = type_adapter.validate_python(user_data).model_dump()
    # вариант фоновой задачи с Celery
    send_comfirmation_email.delay(user_dict, user_data.email)
    # вариант фоновой заддачи с backgroundrasks
    # background_tasks.add_task(send_comfirmation_email, user_dict, user_data.email)
    return user_dict
    
    
@router.post("/login")
async def login_user(response: Response, user_data: SUsers):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectUsernameOrPassword
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("user_acces_token", access_token, httponly=True)
    return access_token

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("user_acces_token")
    
@router.get("/me")
async def read_user_me(curent_user: Users = Depends(get_current_user)):
    return curent_user