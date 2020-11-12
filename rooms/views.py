from django.views.generic import ListView, DetailView
from . import models

# view 는 그url을 통해 view로 들어갈때마다 http request를 생성


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room
