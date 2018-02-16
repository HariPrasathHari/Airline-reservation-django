from django.contrib.auth.models import Group
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

User.objects.all().delete()
User.objects.create_superuser(username='hari',email='hariprasathhari9292@gmail.com', password='harihari')
print('create super user hari')


user_obj = User.objects.create_user(username='user1',email='hariprasathhari9292@gmail.com', password='harihari')
g = Group.objects.get(name='user')
g.user_set.add(user_obj)
print('created user1 ')

staff_obj = User.objects.create_user(username='staff1',email='hariprasathhari9292@gmail.com', password='harihari')
g = Group.objects.get(name='staff')
g.user_set.add(staff_obj)
print('created staff_obj')