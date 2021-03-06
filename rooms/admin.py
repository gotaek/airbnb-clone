from django.contrib import admin
from django.utils.html import mark_safe  # 보안때문에 추가
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


# admin 안에 admin을 넣는 방법, rooms Admin에서 Photos를 볼 수 있게 함
class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    inlines = (PhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),  # 창을 접을 수 있는 기능을 제공
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "guest",
                    "beds",
                    "bedrooms",
                    "baths",
                )
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    # table을 만들어주어서 표시
    list_display = (
        "name",
        "city",
        "country",
        "price",
        "guest",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    # filter 기능을 제공
    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    # 작은 버전의 user admin을 갖게 됨
    raw_id_fields = ("host",)
    # ForiegnKey나 ManyToMany 는 다음과 같이 함수를 정의해 줌으로써 list_display에 추가
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"
    # 검색 기능을 활성화
    search_fields = ("^city", "^host__username")

    # 조금 더 보기좋게 만들어 줌
    filter_horizontal = ("amenities", "facilities", "house_rules")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):

        return mark_safe(f'<img width= "50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
