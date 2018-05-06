# Django LDAP


# 目的
- Djangoの認証にLDAPを利用する


# 環境構築

## Docker
```
$ docker build -t django_ldap .
$ docker run -it -p 8000:8000 --name django_ldap --rm django_ldap /bin/bash
```


## Django
```
$ django-admin startproject django_ldap .


$ vim django_ldap/settings.py
ALLOWED_HOSTS = ['*']
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'


$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK


$ python3 manage.py createsuperuser
Username (leave blank to use 'root'):
Email address:
Password:
Password (again):
Superuser created successfully.


$ python3 manage.py runserver 0.0.0.0:8000
```
