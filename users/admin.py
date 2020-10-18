from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# 이 곳에 무엇을 놓든 admin 패널에서 보여짐
# Register your models here.


@admin.register(models.User)  # admin 패널에서 User를 보고 싶어
class CustomUserAdmin(UserAdmin):  # User를 컨트롤한  클래스가 이게 될거야

    """Custom User Admin"""

    # 필드셋을 다음과 같은 방식으로 커스텀
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
