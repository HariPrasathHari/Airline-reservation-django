"""
* this is a standalone script for creating all groups and each group permissions
* run it as execfile('accounts/group_setup.py')
"""

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Delete all groups
# Delete all permissions assigned to all groups
# this is done to avoid overwritting records in respective tables/models

# create groups
groups = (
    'user',
    'staff',
)

for group in groups:
    g = Group.objects.get_or_create(name=group)
    print('created group ' + group)
# print(g)

# create permissions for groups
# general syntax
"""
content_type = ContentType.objects.get(app_label='myapp', model='BlogPost')
permission = Permission.objects.create(codename='can_publish',
                                       name='Can Publish Posts',
                                       content_type=content_type)
group = Group.objects.get(name='hod')
group.permissions.add(permission)
"""