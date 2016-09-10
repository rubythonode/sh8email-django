from django.core.management.base import BaseCommand, CommandError

from recvmail.recv_server import Sh8MailProcess


class Command(BaseCommand):
    help = 'Run mail receiving server.'

    def handle(self, *args, **options):
        print("SH8EMAIL SMTP SERVER IS START")
        p = Sh8MailProcess()
        p.start()
        print("SH8EMAIL SMTP SERVER IS STARTED")
