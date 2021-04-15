from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import Poll


def home(request):

    return render(request, 'voting/homepage.html')


def votes(request, pk):

    name = Poll.objects.get(id=pk)

    print(name)

    form = VoteForm()

    context = {
        'form': form,
        'name': name
    }

    return render(request, 'voting/votes.html', context)


def results(request, pk):

    name = Poll.objects.get(id=pk)

    dmk = Poll.objects.get(id=1)
    dmk_votes = dmk.no_of_votes

    admk = Poll.objects.get(id=2)
    admk_votes = admk.no_of_votes

    ammk = Poll.objects.get(id=3)
    ammk_votes = ammk.no_of_votes

    mnm = Poll.objects.get(id=4)
    mnm_votes = mnm.no_of_votes

    ntk = Poll.objects.get(id=5)
    ntk_votes = ntk.no_of_votes

    context = {
        'name': name,
        'dmk_votes': dmk_votes,
        'mnm_votes': mnm_votes,
        'ntk_votes': ntk_votes,
        'admk_votes': admk_votes,
        'ammk_votes': ammk_votes,
    }

    if request.method == 'POST':
        name = Poll.objects.get(id=pk)
        name.no_of_votes += 1
        name.save()
        print(name.no_of_votes)

    return render(request, 'voting/results.html', context)