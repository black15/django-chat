from django.shortcuts import render
from account.models import Account
from .models import Message, Room

# Create your views here.
def home(request):
        return render(request, 'chat/home.html')

def search(request):
        context = {}
        if request.method == 'GET':
                search_q = request.GET['friend']
                if len(search_q) > 0:
                        users = Account.objects.filter(username__contains=search_q)
                        # users = Account.objects.all()
                        context['users'] = users
        return render(request, 'chat/home.html', context)

def list_public_chat_rooms(request):
        context = {}

        all_rooms        = Room.objects.all()
        user_rooms       = Room.objects.filter(owner=request.user)

        context['all_rooms']     = all_rooms
        context['user_rooms']    = user_rooms

        return render(request, 'chat/rooms.html', context)

def join_room(request, slug):
        room = Room.objects.get(slug=slug)
        messages         = Message.objects.filter(room=room)[0:20]

        return render(request, 'chat/room.html', {
                'room'          :room,
                'messages'      : messages
        })