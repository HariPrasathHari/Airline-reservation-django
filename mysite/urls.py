from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from mysite.core import views as core_views
from django.conf.urls import url,include
from django.contrib import admin # THIS LINE
from mysite.core.views import home2
admin.autodiscover()

urlpatterns = [
    url(r'^$',home2,name='home2'),
    url(r'^admin/',  admin.site.urls),
    url(r'^book/', include("Airline.urls")),
    url(r'^home/$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^signup_staff/$', core_views.signup_staff, name='staff_signup'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
]
