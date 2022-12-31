from django.shortcuts import render, HttpResponse,redirect
from home.models import About
from datetime import datetime
from django.contrib import messages
from django.views import View

# Create your views here.

context = {
    "Author": "Jawad Ahmed"
}


def index(request):
    return render(request, 'index.html', {"Author":context})
    # return HttpResponse(f"Home Page {id}")


class AboutClass(View):
    def get(self, request):
        return render(request, "about.html", {"data": About.objects.all(),"Author": context})

    def post(self, request):
        print("request.POST",request.POST.get('id'))
        # return HttpResponse("ok")
        if request.POST.get('id',False):
            about = About.objects.filter(id = request.POST.get('id')).first()
            if about:
                # return HttpResponse(about.id)
                about.name = request.POST.get('name')
                about.email = request.POST.get('email')
                about.phone = request.POST.get('phone')
                about.desc = request.POST.get('desc')
                about.save()
                return render(request, "about.html", {"data": About.objects.all(),"Author": context})
            else:
                messages.error(request, 'Data Not Faund')
                return render(request, "about.html", {"data": About.objects.all(),"Author": context})
                
        else:
            about = About(name=request.POST.get('name'), email=request.POST.get('email'), phone=request.POST.get('phone'), desc=request.POST.get('desc'), date=datetime.today())
            about.save()
            messages.success(request, 'Data Added Successfully')
            return render(request, "about.html", {"data": About.objects.all(),"Author": context})
        # return redirect('/about')

    def delete(self, request, id):
        record = About.objects.get(id = id)
        record.delete()
        return render(request, "about.html", {"data": About.objects.all(),"Author": context})
        
def contact(request, id):
    return HttpResponse(f"Contact Page {id}")
