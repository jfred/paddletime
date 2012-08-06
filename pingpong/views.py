from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from pingpong.forms import GameForm
from pingpong.models import Game
from pingpong.models import Player
from pingpong.models import RankChange

def home(request):
    form = GameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('')

    return render_to_response('home.html',
                              {'form':         form,
                               'ranked':       Player.ranked().order_by('rank'),
                               'unranked':     Player.unranked(),
                               'games':        Game.objects.order_by('-timestamp')[:10],
                               'rank_changes': RankChange.objects.order_by('-timestamp')[:10],
                               },
                              context_instance = RequestContext(request))
