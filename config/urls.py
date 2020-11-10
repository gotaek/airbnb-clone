from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # 파일명은 바뀔 수 있기 때문에 파일을 반영한 것을 임포트
from django.conf.urls.static import static  # static 파일을 제공하는 것을 도움


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path("admin/", admin.site.urls),
]
# 만약 개발중이라면 폴더 안의 파일들을 제공
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )  # URL과 folder를 연결
