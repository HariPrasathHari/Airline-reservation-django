# Airline-reservation-django


### Initial setup
```bash
cd to/project/folder/
sudo -s
pip install -r requirements.txt
python manage.py makemigations
python manage.py migrate
python manage.py runserver
```

#### Create superuser
```bash
python manage.py createsuperuser
```

#### To open a shell to open a django shell
```
python manage.py shell
```

#### Setting up test users 
Run this in django shell
```
execfile('setup.py')
```

- create admin 
- add flights in admin page http://127.0.0.1:8000/admin/
- run custom user test setup
- check out each link in website


### Features 
-  Set offer/Disount
-  Book FLight
-  View Bookings
-  admin can see all bookings
-  types of user flight admin and normal user

#### Flight admin
```
username:staff1
password:harihari
```

#### Flight customer
```
username:user1
password:harihari
```
