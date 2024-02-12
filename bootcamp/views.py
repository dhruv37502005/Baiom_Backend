from django.shortcuts import render
from .models import BootCourse, testimonial
from django.views import View
from .models import BootCourse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
def BootCamp(request):
    courses = BootCourse.objects.all()
    testimonials = testimonial.objects.all()
    return render(request,'Wep.html',{'courses':courses , 'testimonials':testimonials})


class DownloadFileView(View):
    def get(self,request, *args, **kwargs):
        bootcamp = get_object_or_404(BootCourse,is_wep_main =True)
        file_content = bootcamp.brochure.read()
        file_name = bootcamp.brochure.name
        response = HttpResponse(file_content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

        return response