from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Room


def index(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        if name:
            room = Room.objects.create(name=name, host=request.user)
            print(room.pk)
            return HttpResponseRedirect(reverse("room", kwargs={"pk": room.pk}))
    return render(request, 'index.html')


def room(request, pk):
    room: Room = get_object_or_404(Room, pk=pk)
    return render(request, 'room.html', {
        "room": room,
    })


