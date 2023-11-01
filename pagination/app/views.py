from django.core.paginator import Paginator
from django.shortcuts import render
from app.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    paginator = Paginator( posts,1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{"page_obj": page_obj})