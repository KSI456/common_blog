from django.http.request import RAISE_ERROR
from django.shortcuts import render, redirect, get_object_or_404
# View에 Model(Post 게시글) 가져오기
from .models import Post, Photo, Comment
from .forms import CommentForm, PostForm
# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    commentlist = Comment.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'main/blog.html', {'postlist':postlist, 'commentlist':commentlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    postlist = Post.objects.get(pk=pk)
    photolist = postlist.photo_set.all()
    commentlist = postlist.comment.all()
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'postlist':postlist, 'photolist':photolist,'commentlist':commentlist})

def new_post(request):
    if request.method == 'POST':
        post = Post()
        post.postname = request.POST['postname']
        post.contents = request.POST['contents']
        post.save()
        for img in request.FILES.getlist('mainphoto'):
            photo = Photo()
            photo.post = post
            photo.image = img
            photo.save()
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})

def comment(request,pk):
    if request.method =='POST':
        com = Comment()
        post = Post(request, pk=pk)
        com.related_post=post
        com.comment_user=request.POST.get('comment_user')
        com.comment=request.POST.get('comment')
        com.password=request.POST.get('password')
        com.created_date=request.POST.get('created_date')
        com.save()
        return redirect('/blog/{}/'.format(pk))
    return render(request, 'main/posting.html')

def del_comment(request,pk,pk2):
    comment = Comment.objects.get(pk=pk2)
    if request.method == 'POST':
        if request.POST['password'] and request.POST['password'] == comment.password:
            comment.delete()
        else:
            return render(request, 'main/incorrect_password.html')
        return redirect('/blog/{}'.format(pk))
    return render(request, 'main/posting.html')