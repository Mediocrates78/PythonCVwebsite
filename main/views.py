from django.shortcuts import render
from datetime import date
import random as rnd
from main.functions import *

def home(request):
    current = date.today()
    bday = date(1978, 3, 13)
    age = current.year - bday.year
    if current.month < bday.month:
        age -= 1
    elif current.month == bday.month and current.day < bday.day:
        age -= 1
    return render(request, 'main/index.html', {'age': age})

def fun(request):
    return render(request, 'main/fun.html', {})

def lowest(request):
    context = {'result': None, 'random': ['', '', '', '', '', '', '']}
    if request.POST.get('lowest_submit') == 'Random':
        context['random'] = [rnd.randint(1, 99) for i in range(7)]
    if request.POST.get('lowest_submit') == 'Submit':
        no1 = request.POST.get('no1')
        no2 = request.POST.get('no2')
        no3 = request.POST.get('no3')
        no4 = request.POST.get('no4')
        no5 = request.POST.get('no5')
        no6 = request.POST.get('no6')
        no7 = request.POST.get('no7')
        temp_list = [no1, no2, no3, no4, no5, no6, no7]
        my_list = [i for i in temp_list if i != '' and i != None]
        context['result'] = find_lowest(my_list)
    return render(request, 'main/lowest.html', context)

def encoder(request):
    unencoded = ""
    encoded = ""
    if request.POST.get("encoding_button") == "Encode":
        uncoded = request.POST.get('uncoded')
        encoded = request.POST.get('encoded')
        encoded = encoding(uncoded)
    if request.POST.get("encoding_button") == "Decode":
        uncoded = request.POST.get('uncoded')
        encoded = request.POST.get('encoded')
        unencoded = decoding(encoded)
    context = {'encoder': [unencoded, encoded]}
    return render(request, 'main/encoder.html', context)

def path(request):
    butts = [i for i in range(20)]
    context = {'butts': butts}
    return render(request, 'main/path.html', context)
