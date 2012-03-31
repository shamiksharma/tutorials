
from mixpanel.tasks import EventTracker
import settings

from django.http import HttpResponse

def index(request):
    et = EventTracker()
    et.run('dj_event', {'distinct_id': 1}, token=settings.token )
    return HttpResponse("Hello, world!.")
