# Create your views here.
import datetime
import random
import string

from django.views.generic import TemplateView

from web.models import UserAction


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        # ip = request.META.get('REMOTE_ADDR') # Not 127.0.0.1
        import socket
        import struct
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    return ip


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        user = UserAction()
        email = f'{random_char(6)}@gmail.com'
        user.email = email
        user.ip = get_client_ip(self.request)
        user.timestamp = datetime.datetime.now()
        user.country_code = random.choices(UserAction.COUNTRY_CODE)[0][0]
        user.save()
        context.update({
            'user': user,
        })
        return context
