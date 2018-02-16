from django import forms
from django.contrib.admin.widgets import AdminDateWidget




class FlightForm(forms.Form):
    From = forms.CharField(max_length=100,label='From ',required=False)
    To = forms.CharField(max_length=100,label='Destination',required=False)
    no = forms.IntegerField(max_value=5,  min_value=1, label='Number of tickets',initial=1)
    # From_date = forms.DateField(widget=AdminDateWidget)
    # To_Date = forms.DateField(widget=AdminDateWidget,required=False)

class PaymentForm(forms.Form):
    ac_no = forms.IntegexrField(min_value=100000000000,max_value=999999999999,label='Credit card/ Debit Card')



class OfferForm(forms.Form):
    off = forms.IntegerField(min_value=0,max_value=90,label='OFFER')


class UserDetailForm(forms.Form):
    Name = forms.CharField(max_length=10)
    Age = forms.IntegerField(min_value=0 ,max_value=100)