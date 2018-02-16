from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.db import transaction


from .forms import FlightForm, PaymentForm, OfferForm, UserDetailForm
from .models import *


@login_required()
def find_flight(request,**kwargs):
    print('method called')
    user = request.user
    current_site = get_current_site(request)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FlightForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('checked')
            list_of_flights = dict()
            list_of_flights['list_of_flight'] = Travelling.objects.filter(from_place__contains=form.cleaned_data['From']).filter(to_place__contains=form.cleaned_data['To']).filter(available__gte=form.cleaned_data['no'])
            list_of_flights['form'] = FlightForm()
            list_of_flights['domain'] = current_site
            list_of_flights['number'] = form.cleaned_data['no']
            list_of_flights['permissions'] = user.is_staff
            print(list_of_flights)

            return render(request, 'result.html', list_of_flights)
            # return HttpResponseRedirect('list')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FlightForm()

    return render(request, 'flights.html', {'form': form, 'permissions': user.is_staff})


@login_required()
@transaction.atomic
def book_flight(request,**kwargs):
    no = kwargs.pop("no_seats")
    fl = kwargs.pop("travel_id")
    print(no,fl)
    travel_obj = Travelling.objects.get(id=fl)
    off_rate = int(travel_obj.rate-(travel_obj.off*travel_obj.rate/100))
    print(off_rate)
    list_form = []
    for i in range(int(no)):
        list_form.append(UserDetailForm())

    context = dict()
    context['offrate'] = off_rate
    context['list_form'] = list_form
    context['seats'] = no
    context['flight_id'] = fl
    context['flight'] = travel_obj
    print(no,off_rate,str(int(no)*int(off_rate)))
    context['total'] = int(no)*int(off_rate)
    form = PaymentForm()
    context['form'] = form
    print(context)
    if request.method == 'POST':
        print('form requested')

        # create a form instance and populate it with data from the request:
        form = PaymentForm(request.POST)
        lis = []
        for i in range(int(no)):
            lis.append(UserDetailForm(request.POST))
        # check whether it's valid:
        if form.is_valid():
            for i in range(int(no)):
                if not lis[i].is_valid():
                    pass
                    return render(request,'pay.html',context)
            print(lis)
            print('form valid')
            with transaction.atomic():
                if int(travel_obj.available) > int(no):
                    travel_obj.available = int(travel_obj.available) - int(no)
                    travel_obj.collected = int(travel_obj.collected) + int(off_rate)
                    travel_obj.save()
                    obj_list= []
                    obj = Booking.objects.create(no_of_seats=no, Travelling=travel_obj, booked=request.user,cost=off_rate)
                    for i in range(int(no)):
                        name = lis[i].cleaned_data['Name']
                        age = lis[i].cleaned_data['Age']
                        x = UserAge.objects.create(name=name, age=age,booked=obj)
                        print(x)
                    return render(request, 'done.html', context)
                else:
                    return HttpResponseRedirect('/book')
        # return HttpResponseRedirect('list')
    return render(request, 'pay.html', context)


@login_required()
def view_all_booking(request):
    if request.user.is_staff:
        pass
    else:
        return render(request,'permission_error.html')
    qs = Booking.objects.all()
    context = dict()
    context['my_booking'] = qs
    return render(request, 'view_all_booking.html', context)


@login_required()
def view_my_booking(request):
    user = request.user
    qs = Booking.objects.filter(booked=user)
    a = {}
    for i in qs:
        qss = UserAge.objects.filter(booked=i)
        a[i] = qss
    context = dict()
    context['my_booking'] = qs
    context['people'] = a
    print(context)
    print(a)
    return render(request, 'view__booking.html', context)


@login_required()
def set_offer(request,**kwargs):
    user_obj = request.user
    if user_obj.is_staff:
        pass
    else:
        return render(request,'permission_error.html')
    id = kwargs.pop("id")
    qs = Travelling.objects.get(id=id)
    context = dict()
    context['my_booking'] = qs

    form = OfferForm()
    context['form'] = form
    if request.method == 'POST':
        print('post in')
        form = OfferForm(request.POST)
        if form.is_valid():
            print('in form')
            off = form.cleaned_data['off']
            qs.off = off
            qs.save()
            return HttpResponseRedirect('/book/off_list/')
    return render(request, 'set_offer.html', context)

