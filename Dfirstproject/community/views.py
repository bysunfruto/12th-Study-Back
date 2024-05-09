from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import *
from .Forms import QuestionForm, CommentForm


# Create your views here.

def list(request):
    posts = Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Question, pk=pk)
    post_hashtag=post.hashtag.all()
    return render(request, 'detail.html', {'post':post, 'hashtags':post_hashtag})

def new(request):
    form=QuestionForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form=QuestionForm(request.POST, request.FILES)
    if form.is_valid():
        new_question=form.save(commit=False)
        new_question.upload_time=timezone.now()
        new_question.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_question.hashtag.add(new_hashtag[0])
        return redirect('detail', new_question.id)
    return redirect('list')

    # new_question=Question()
    # new_question.title=request.POST['title']
    # new_question.content=request.POST['content']
    # new_question.upload_time=timezone.now()
    # new_question.save()
    # return redirect(List)

def delete(request, pk):
    question_delete=get_object_or_404(Question, pk=pk)
    question_delete.delete()
    return redirect('list')

def update_page(request, pk):
    question_update=get_object_or_404(Question, pk=pk)
    return render(request, 'update.html', {'post':question_update})

def update(request, pk):
    question_update = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', '')  
        content = request.POST.get('content', '')  
        question_update.title = title
        question_update.content = content
        question_update.save()
        return redirect('list')
    else:
        return render(request, 'update.html', {'post': question_update})
    
def add_comment(request, pk):
    community=get_object_or_404(Question, pk=pk)

    if request.method=='POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=community
            comment.save()
            return redirect ('detail', pk)
        
    else:
        form=CommentForm()

    return render(request, 'add_comment.html', {'form':form})

def like_post(request, pk):
    # 게시물 가져오기
    try:
        post = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("게시물을 찾을 수 없습니다.")

    # 이미 좋아요를 눌렀는지 확인
    already_liked = Like.objects.filter(post=post, username=request.user.username).exists()

    if already_liked:
        # 이미 좋아요를 누른 상태이면 좋아요 취소
        Like.objects.filter(post=post, username=request.user.username).delete()
        post.likes_count -= 1
        post.save()
    else:
        # 좋아요 추가
        Like.objects.create(post=post, username=request.user.username)
        post.likes_count += 1
        post.save()

    # 상세 페이지로 리다이렉트
    return redirect('detail', pk=pk)
