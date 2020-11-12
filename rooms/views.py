from django.view.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render  # html을 return할 수 있게 함
from django.views.generic import ListView
from . import models

# view 는 그url을 통해 view로 들어갈때마다 http request를 생성


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


# http response를 반환해야함
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()