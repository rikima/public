"""
Active Directory対応の認証バックエンド
Active DirectoryのユーザーIDとパスワードで認証を行う
認証以外の認可等は、対応しない
参考URL https://docs.djangoproject.com/en/2.0/topics/auth/customizing/
"""

from ssl import CERT_NONE, PROTOCOL_SSLv23
from ldap3 import Server, Connection, Tls

from django.conf import settings
from django.contrib.auth.models import User


class Backend:
    """
    Active Directory用の認証バックエンドクラス

    settings.pyに以下を設定することで、本バックエンドを変更している
    AUTHENTICATION_BACKENDS = ['django_ldap.backend.Backend']
    LDAP_HOST = 'your-ldap-host-ip-address'
    LDAP_PORT = 636
    LDAP_DOMAIN = 'your-ldap-domain'
    """

    def authenticate(self, request, username=None, password=None):
        """
        独自バックエンドに必須のメソッド

        Active Directoryへusernameとpasswordでbindして認証を実施
        該usernameがDjangoに存在しない場合は、新規作成する必要がある
        """

        if not (username and password):
            return None

        tls = Tls(validate=CERT_NONE, version=PROTOCOL_SSLv23)
        server = Server(host=settings.LDAP_HOST, port=settings.LDAP_PORT, use_ssl=True, tls=tls)
        connection = Connection(
            server,
            user='{}\\{}'.format(settings.LDAP_DOMAIN, username),
            password=password)
        if not connection.bind():
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
        """
        独自バックエンドに必須のメソッド

        参考URLと同じ
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
