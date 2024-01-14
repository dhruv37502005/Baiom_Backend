from django.http import HttpResponseRedirect
from django.urls import reverse
from baoiam import settings
from .models import MaintenancePage


def maintenance_middleware(get_response):
    def middleware(request):
        #before the middleware
        if page_is_enabled('Maintenance Break'):
            if request.path != reverse('maintenance'):
                if '/admin/' not in request.path:
                    if settings.STAGING != 'True':
                        return HttpResponseRedirect(reverse('maintenance'))
            
        # if page_is_enabled('Staging'):
        #     if request.path != reverse('locked'):
        #         if '/admin/' not in request.path:
        #             if settings.STAGING == 'True':
        #                 if 'staging_access' not in request.session:
        #                     return HttpResponseRedirect(reverse('locked'))
            
        response=get_response(request)
        return response
    return middleware

def page_is_enabled(page_name):
    page = MaintenancePage.objects.filter(name=page_name).first()
    if page:
        return page.is_enabled
    else:
        return False