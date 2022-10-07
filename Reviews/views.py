from django.shortcuts import render,redirect
from .models import Review
from .forms import ReviewForm
# Create your views here.

def index(request):
    k = Review.objects.all()
    context = {
        "v":k
    }
    return render(request,"Reviews/index.html", context)

def create(request):
    if request.method == "POST":
        Review_Form = ReviewForm(request.POST)
        if Review_Form.is_valid():
            Review_Form.save()
            return redirect("/")
    else:
        Review_Form = ReviewForm()
    return render(request, "Reviews/create.html",{"Review_Form":Review_Form})

def detail(request, pk):
    k = Review.objects.get(pk = pk)
    return render(request, "Reviews/detail.html", {"v":k})

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("/")

def update(request, pk):
    k = Review.objects.get(pk=pk)
    if request.method == "POST":
        Review_Form = ReviewForm(request.POST, instance=k)
        if Review_Form.is_valid():
            Review_Form.save()
            return redirect("/")
    else:
        Review_Form = ReviewForm(instance=k)
    return render(request, "Reviews/update.html",{"Review_Form":Review_Form ,"v":k})
