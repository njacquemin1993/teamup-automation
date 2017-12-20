from django.utils import timezone

def server_info(request):
    now = timezone.localtime()
    return {"SERVER_TIME" : now}
