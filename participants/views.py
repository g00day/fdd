from django.shortcuts import render, get_object_or_404
from .models import Participant

def participants_list(request):
    participants = Participant.objects.all()
    # Рендерим простой список участников по аналогии с мероприятиями
    return render(request, 'participants_list.html', {'participants': participants})

def participant_detail(request, part_id):
    participant = get_object_or_404(Participant, id=part_id)
    photos = participant.photos.all()  # Обратная связь ManyToMany (отметки людей)
    return render(request, 'participant_detail.html', {'participant': participant, 'photos': photos})
