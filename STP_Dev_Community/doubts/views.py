from django.shortcuts import render, get_object_or_404, redirect
from .models import Doubt, Comment

def home(request):
    doubts = Doubt.objects.all().order_by("-created_at")
    return render(request, "home.html", {"doubts": doubts})

def doubt_detail(request, pk):
    doubt = get_object_or_404(Doubt, pk=pk)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(doubt=doubt, author=request.user, content=content)
        return redirect("doubts:doubt_detail", pk=pk)
    return render(request, "doubt_detail.html", {"doubt": doubt})

def create_doubt(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        author = request.user
        if title and description:
            Doubt.objects.create(
                title=title, description=description, image=image, author=author
            )
        return redirect("doubts:home")
    return render(request, "create_doubt.html")
