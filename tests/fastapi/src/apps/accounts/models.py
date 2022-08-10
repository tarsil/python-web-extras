from python_web_extras.fastapi.models import User as AbsUser


class User(AbsUser):
    class Meta:
        table = "users"
