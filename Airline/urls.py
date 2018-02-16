from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from Airline.models import Booking,Travelling
from Airline.views import *
urlpatterns = [
                url(r'^$', find_flight, name='find_flight'),
                url(r'^flight/(?P<no_seats>[\w-]+)/(?P<travel_id>[\w-]+)/$', book_flight,name='book_flight'),
                url(r'^view_book/$', view_my_booking,name='view_my_booking'),
                url(r'^view_all_book/$', view_all_booking,name='view_all_booking'),
                url(r'^set_offer/(?P<id>[\w-]+)/$', set_offer, name='set_offer'),
                url(r'^off_list/$', ListView.as_view(
                                    queryset=Travelling.objects.all(),
                                    template_name="set_offer_list.html"),name='off_list'),

            ]