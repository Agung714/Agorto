from django.shortcuts import render
from .models import Portofolio
# from .models import HomeImage

# Create your views here.
def home(request):
    portofolio = Portofolio.objects.all()
    # Portofolio.
    context = {
        'Portofolio': portofolio,
    }
    return render(request, 'homepage/cv.html',context)
    # return render(request, 'home.html', {'content': content, 'services': services})
 