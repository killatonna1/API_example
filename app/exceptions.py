from fastapi import HTTPException, status

UserAlredyExistsException = HTTPException(
    status_code= status.HTTP_409_CONFLICT,
    detail="User alredy exists, please enter another email",
)

IncorrectUsernameOrPassword = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="wrong email or password",
)