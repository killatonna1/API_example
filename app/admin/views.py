
from sqladmin import Admin, ModelView

from app.registration.models import Users



class UserAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    category = "Аккаунты"
    column_details_exclude_list = [Users.password]
    
    