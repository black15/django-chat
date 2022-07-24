from operator import is_
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from account.models import Account, FriendRequest
from .forms import UserRegisterForm, UpdateUserInfo

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'User created succesfuly!')
             return redirect('account:login')
    else:
        form = UserRegisterForm()

    return render(request, 'account/register.html', {'formFromViews': form})

@login_required
def account_view(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get('user_id')
    try:
        account      = Account.objects.get(pk=user_id)
        frequests    = FriendRequest.objects.filter(to_user=request.user)
    except:
        return HttpResponse('User does not exist !')
    if account:
        context['id']           = account.id
        context['username']     = account.username
        context['email']        = account.email
        context['bio']          = account.bio
        context['profile_img']  = account.profile_img
        context['hide_email']   = account.hide_email
        
        friends = []
        for friend in request.user.friends.all():
            friends.append(friend)
        context['friends_n']      = len(friends)

        fr_friends = []
        for friend in account.friends.all():
            fr_friends.append(friend)
        context['fr_friends_n']      = len(fr_friends)


        is_self     = True
        is_friend   = False
        user        = request.user
        if user.is_authenticated and user != account:
            is_self = False
        elif not user.is_authenticated :
            is_self = False

        context['is_self']      = is_self
        context['is_friend']    = is_friend
        # context['BASE_URL']     = settings.BASE_URL

        context['frequest']     = frequests
        context['frequest_n']   = len(frequests)

    return render(request, 'account/account.html', context)

@login_required
def edit(request, user_id):
    if not request.user.is_authenticated:
        return redirect('account:login')
    try:
        form = UpdateUserInfo()
        account = Account.objects.get(id=user_id)
    except:
        return HttpResponse('User does not exist !')

    if request.method == "POST":
        if account.id == request.user.id:
            form = UpdateUserInfo(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect(reverse('account:profile', args=[request.user.id]))
        else:
            form = UpdateUserInfo(instance=request.user)

    return render(request, 'account/edit_account.html', {'form': form})

def send_friend_request(request, id):
    from_user   = request.user
    to_user     = Account.objects.get(id=id)
    frequest    = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    return redirect(reverse('account:profile', args=[request.user.id]))


def accept_friend_request(request, id):
    frequest    = FriendRequest.objects.get(id=id)
    sender      = request.user
    receiver    = frequest.from_user

    sender.friends.add(receiver)
    receiver.friends.add(sender)

    frequest.delete()

    return redirect(reverse('account:list-friends', args=[request.user.id]))

@login_required
def list_friends(request, user_id):
    context = {}

    is_self     = False
    if request.user.is_authenticated:
        is_self = True
    friends     = request.user.friends.all()

    context['friends'] = friends
    context['is_self'] = is_self

    return render(request, 'account/friends.html', context)

def list_friend_requests(request, user_id):
    context = {}

    frequest    = FriendRequest.objects.filter(to_user=request.user)
    is_self     = False
    if request.user.is_authenticated:
        is_self = True

    context['frequests']= frequest
    context['is_self']  = is_self

    return render(request, 'account/friends.html', context)

def remove_friend(request, user_id):
    remover      = request.user
    removee      = Account.objects.get(id=user_id)

    remover.friends.remove(removee)
    removee.friends.remove(remover)

    return redirect(reverse('account:list-friends', args=[request.user.id]))
