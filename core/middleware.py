from datetime import datetime, timedelta
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from baoiam import settings
from .models import MaintenancePage

def maintenance_middleware(get_response):
    def middleware(request):
        if page_is_enabled('Maintenance Break'):
            if request.path != reverse('maintenance'):
                if '/admin/' not in request.path:
                    if settings.STAGING != 'True':
                        maintenance_page = MaintenancePage.objects.filter(name='Maintenance Break').first()
                        remaining_time = calculate_remaining_time(maintenance_page.end_time)
                        if remaining_time.total_seconds() > 0:
                            maintenance_template = loader.get_template('maintenance_break.html')
                            maintenance_content = maintenance_template.render({
                                'hours': remaining_time.seconds // 3600,
                                'minutes': (remaining_time.seconds // 60) % 60,
                                'seconds': remaining_time.seconds % 60
                            })
                            return HttpResponse(maintenance_content, status=503)

        response = get_response(request)
        return response

    return middleware

def calculate_remaining_time(end_time):
    now = timezone.now()
    
    if end_time is not None:
        remaining_time = end_time - now
        return max(remaining_time, timedelta(0))
    else:
        return timedelta(0)

def page_is_enabled(page_name):
    page = MaintenancePage.objects.filter(name=page_name).first()
    if page:
        return page.is_enabled
    else:
        return False








# def maintenance_middleware(get_response):
#     def middleware(request):
#         #before the middleware
#         if page_is_enabled('Maintenance Break'):
#             if request.path != reverse('maintenance'):
#                 if '/admin/' not in request.path:
#                     if settings.STAGING != 'True':
#                         return HttpResponseRedirect(reverse('maintenance'))
            
#         # if page_is_enabled('Staging'):
#         #     if request.path != reverse('locked'):
#         #         if '/admin/' not in request.path:
#         #             if settings.STAGING == 'True':
#         #                 if 'staging_access' not in request.session:
#         #                     return HttpResponseRedirect(reverse('locked'))
            
#         response=get_response(request)
#         return response
#     return middleware

# def page_is_enabled(page_name):
#     page = MaintenancePage.objects.filter(name=page_name).first()
#     if page:
#         return page.is_enabled
#     else:
#         return False