from django.conf import settings

from main.models import Wod

import subprocess
import mechanize

LOGIN_URL = "https://goteamup.com/p/787790-crossfit-vetroz/auth/?next=/p/787790-crossfit-vetroz/"

def register_for_wod(uuid):
    wod = Wod.objects.get(uuid=uuid)

    wod_url = wod.wod_url

    b = mechanize.Browser()
    b.open(LOGIN_URL)
    b.select_form(nr=0)
    b.form["email"] = wod.user.email
    b.form["password"] = wod.user.first_name
    b.submit()
    b.open(wod_url)
    b.select_form(nr=0)
    b.submit()
    wod.launched = True
    wod.save()


