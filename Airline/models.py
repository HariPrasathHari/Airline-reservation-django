from django.db import models
from django.contrib.auth.models import User



class Travelling(models.Model):
    flight = models.CharField(max_length=30)
    from_place = models.CharField(max_length=30)
    to_place = models.CharField(max_length=30)
    depart_at_from = models.TimeField()
    arrival_at_to = models.TimeField()
    seat_no = models.IntegerField()
    available = models.IntegerField()
    rate = models.IntegerField()
    off = models.IntegerField()
    collected = models.IntegerField(default=0)

    def __str__(self):
        return str(self.flight)+str(self.from_place)+str(self.to_place) + str(self.depart_at_from) + str(self.arrival_at_to)



class Booking(models.Model):
    booked = models.ForeignKey(User)
    no_of_seats = models.IntegerField()
    Travelling = models.ForeignKey(Travelling)
    cost = models.IntegerField(default=0)
    def __str__(self):
        return str(self.Travelling)+str(self.booked)+str(self.no_of_seats)


class UserAge(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    booked = models.ForeignKey(Booking)
