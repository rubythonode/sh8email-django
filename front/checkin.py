class CheckinManager(object):
    def __init__(self, request):
        self.request = request

    def current_recipient(self):
        return self.request.session.get('recipient')

    def set_current_recipient(self, recipient):
        self.request.session['recipient'] = recipient
