from django.contrib.auth.models import AbstractUser
from django.db import models

# 장고는 models 파일을 확인 후 migration파일을 생성함
# 원하는 DataBase가 어떻게 생겼는지 설명하는 곳


class User(AbstractUser):  # AbstractUser를 상속받았기 때문에 migrations에 ID, Password 등이 있는 것

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    # 선택지를 만들고 싶을 때 사용
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Femalie"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISG = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISG, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # model파일의 필드
    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
