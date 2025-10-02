from django.shortcuts import render
from .models import Coffee  # ✅ Import the Coffee model
# views.py
def Home(request):
    from .models import Coffee
    coffeelist = Coffee.objects.all()
    print("✅ Rendering template: home.html")  # ← Add this
    return render(request, 'home.html', {'coffeelist': coffeelist})

def index(request):
    return render(request, 'index.html')