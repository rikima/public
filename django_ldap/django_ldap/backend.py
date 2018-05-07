from ssl import CERT_NONE, PROTOCOL_SSLv23
from ldap3 import Server, Connection, Tls

from django.conf import settings
from django.contrib.auth.models import User


class Backend:


    def authenticate(self, request, username=None, password=None):

        if not (username and password):
            return None

        tls = Tls(validate=CERT_NONE, version=PROTOCOL_SSLv23)
        server = Server(host=settings.LDAP_HOST, port=settings.LDAP_PORT, use_ssl=True, tls=tls)
        conn = Connection(server, user='{}\\{}'.format(settings.LDAP_DOMAIN, username), password=password)
        if not conn.bind():
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        return user


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
