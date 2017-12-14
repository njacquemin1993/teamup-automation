from django.conf import settings

from main.models import Wod

import subprocess

DEFAULT_BASH_ENV = {"PATH" : "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" }

def register_for_wod(uuid):
    wod = Wod.objects.get(uuid=uuid)
    session_id = wod.user.first_name
    profile, membership = wod.user.last_name.split("|")
    csrf_token = "12345678123456781234567812345678"
    wod_url = wod.wod_id
    cmd = """curl '{wod_url}register/' -H 'Referer: {wod_url}' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: sessionid={session_id}; csrftoken={csrftoken}' --data 'csrfmiddlewaretoken={csrftoken}&status=book&due_now_price=0&consumerprofile={profile}&consumermembership={membership}'""".format(**locals())
    subprocess.check_output(cmd, cwd="/tmp", env=DEFAULT_BASH_ENV, stderr=subprocess.STDOUT, shell=True, executable="/bin/bash")


