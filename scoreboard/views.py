from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from scoreboard.models import User, Score, Size
from scoreboard.forms import AddScore


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


def user(request, userid):
    template = loader.get_template('user.html')
    user = User.objects.get(id=userid)
    scores_list = Score.objects.filter(player_id=userid)
    sizes_list = Size.objects.all()
    return HttpResponse(template.render({
        "user": user,
        "scores": scores_list,
        "sizes": sizes_list
    }))


def sizes(request):
    template = loader.get_template('sizes.html')
    users_list = User.objects.all()
    sizes_list = Size.objects.all()
    scores_list = Score.objects.all()
    top5_size_list = []
    for size in sizes_list:
        top5_size_list.append({"size": size,
                               "score": Score.objects.filter(length=size.length, height=size.height, mines=size.mines).order_by(
                                   'duration')[:5]
                               })

    return HttpResponse(template.render({
        "users": users_list,
        "scores": scores_list,
        "sizes": sizes_list,
        "top5_list": top5_size_list
    }))


def addscore(request):
    template = loader.get_template('newscore.html')
    if request.method =="POST":
        form = AddScore(request.POST)
        if form.is_valid():
            return HttpResponse(template.render({
                "form": form
            }))
    else:
        form = AddScore()
    return HttpResponse(template.render({
        "form": form
    }))




