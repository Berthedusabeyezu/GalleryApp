from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Location,Category

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request, 'welcome.html',{"images":images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-galleries/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-galleries/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-galleries/image.html", {"image":image})  

def location(request,location_id):
    location=Location.objects.get(id = location_id)
    images = Image.objects.filter(location =location.id)
    
    return render(request,'location.html',{'location':location,'images':images})  
