from email.message import EmailMessage

from app.config import settings

from pydantic import EmailStr

def create_new_message(
    registration_info: dict,
    email_to: EmailStr
):
    email = EmailMessage()
    email["Subject"] = "Подтверждение регистрации"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to
    
    email.set_content(
        f"""
        <h1> Comformation gps App registration<h1>
        You have successfully registered! Your email: {registration_info["email"]}
        """,
        subtype="html"
        
    )
    return email