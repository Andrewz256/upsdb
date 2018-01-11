from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import UPSB, Battery
from .forms import PostBat, PostUPS
from django.db.models import Q

def index(request):
    UPS_battery_list = UPSB.objects.order_by('-dateU')
    context1 = {'UPS_battery_list': UPS_battery_list}
    return render(request, 'ups/index.html', context1)

def batteries(request):
    Battery_list = Battery.objects.order_by('obitBN')
    context2 = {'Battery_list': Battery_list}
    return render(request, 'ups/battery.html', context2)

def upsnew(request):
    if request.method == "POST":
        Form_ups = PostUPS(request.POST)
        if Form_ups.is_valid():
           ups = Form_ups.save(commit=False)
           ups.dateU = timezone.now()
           ups.save()
           return redirect('/')
    else:
        Form_ups = PostUPS()
    return render(request, 'ups/ups_edit.html', {'Form_ups': Form_ups}) 

def batnew(request):
    if request.method == "POST":
        Form_bat = PostBat(request.POST)
        if Form_bat.is_valid():
           bat = Form_bat.save(commit=False)
           bat.dateB = timezone.now()
           bat.save()
           return redirect('/battery')
    else:
       Form_bat = PostBat()
    return render(request, 'ups/bat_edit.html', {'Form_bat': Form_bat})

def get_ups_list(request):
    error = []
    if 'q' in request.GET:
       q = request.GET['q']
       if not q:
          error.append('Enter something in search query,  dumb.')
       else:
          lookups = Q(obitN__icontains=q)| Q(obitInsBat1__obitBN__icontains=q)| Q(obitInsBat2__obitBN__icontains=q)| Q(obitOutBat1__obitBN__icontains=q)| Q(obitOutBat2__obitBN__icontains=q)| Q(dateU__date=q)
          search_ups_list = UPSB.objects.filter(lookups).distinct()
          return render_to_response('ups/search.html', {'search_ups_list' : search_ups_list, 'query': q})
    return render_to_response('ups/index.html', {'error': error})

def get_battery_list(request):
    error = []
    if 'q' in request.GET:
       q = request.GET['q']
       if not q:
          error.append('Enter something in search query,  dumb.')
       else:
          lookups = Q(obitBN__icontains=q)| Q(dateB__date=q)
          search_battery_list = Battery.objects.filter(lookups).distinct()
          return render_to_response('ups/searchb.html', {'search_battery_list' : search_battery_list, 'query': q})
    return render(request, 'ups/battery.html', {'error': error})


def ups_edit(request, id_s):
    ups = get_object_or_404(UPSB, id=id_s)
    if request.method == "POST":
        Form_ups = PostUPS(request.POST, instance=ups)
        if Form_ups.is_valid():
           ups = Form_ups.save(commit=False)
           ups.save()
           return redirect('/')
    else:
       Form_ups = PostUPS(instance=ups)
    return render(request, 'ups/ups_edit.html', {'Form_ups': Form_ups})

def bat_edit(request, id_s):
    bat = get_object_or_404(Battery, obitBN=id_s)
    if request.method == "POST":
        Form_bat = PostBat(request.POST, instance=bat)
        if Form_bat.is_valid():
           bat = Form_bat.save(commit=False)
           bat.dateB = timezone.now()
           bat.save()
           return redirect('/battery')
    else:
       Form_bat = PostBat(instance=bat)
    return render(request, 'ups/bat_edit.html', {'Form_bat': Form_bat})


def ups_remove(request, id_s):
    ups = get_object_or_404(UPSB, id=id_s)
    ups.delete()
    return redirect('/')

def bat_remove(request, id_s):
    bat = get_object_or_404 (Battery, obitBN=id_s)
    bat.delete()
    return redirect('/battery')

