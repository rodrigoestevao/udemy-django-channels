from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request):
    room_no = request.POST["room_no"]
    name = request.POST["name"]
    context = {
        "room_no": room_no,
        "name": name,
    }
    return render(request, "chat/room.html", context=context)
