from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from scoreboard.models import User, Score, Size

# Create your views here.


def users(request):
    template = loader.get_template('users.html')
    users_list = User.objects.all()
    sizes_list = Size.objects.all()
    scores_list = Score.objects.all()
    return HttpResponse(template.render({
        "users": users_list,
        "scores": scores_list,
        "sizes": sizes_list
    }))
