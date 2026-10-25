from django.shortcuts import render, get_object_or_404
from .models import Event

def events_list(request):
    events = Event.objects.all()
    return render(request, 'events_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    albums = event.albums.all()
    return render(request, 'event_detail.html', {'event': event, 'albums': albums})
