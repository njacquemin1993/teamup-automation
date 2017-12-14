from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from main.models import Wod
from main.tasks import register_for_wod
from django.conf import settings

import time

def check_wod():
    print("Checking...")
    now = timezone.now()
    for wod in Wod.objects.filter(launch_time__lte=now, launched=False):
        register_for_wod(wod.uuid)
        wod.launched = True
        wod.save()        

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            while True:
                check_wod()
                time.sleep(60)
        except (KeyboardInterrupt, SystemExit):
            pass
