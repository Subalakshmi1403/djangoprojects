from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.
def allpost(request):
    post = Post.objects
    return render(request,'posts.html',{'post':post})

def detial(request,blog_id):
    detial = get_object_or_404(Post,pk = blog_id)
    return render(request,'detials.html',{'post':detial})