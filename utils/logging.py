from django.core import mail
from django.core.mail import get_connection
from django.utils.log import AdminEmailHandler


class NonSilentAdminEmailHandler(AdminEmailHandler):
    def send_mail(self, subject, message, *args, **kwargs):
        mail.mail_admins(subject, message, *args, connection=self.connection(), fail_silently=False, **kwargs)

    def connection(self):
        return get_connection(backend=self.email_backend, fail_silently=False)