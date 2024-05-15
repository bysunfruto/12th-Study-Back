from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import Question
from .forms import QuestionForm, CommentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Question
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def List(request):
    questions = Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'home.html', {'questions':questions})


def detail(request, pk):
    question_detail = get_object_or_404(Question, pk=pk)
    question_hashtag=question_detail.hashtag.all()
    return render(request, 'detail.html', {'question':question_detail, 'hashtags':question_hashtag})

def new(request):
    form=QuestionForm()
    return render(request, 'new.html',{'form':form})

def create(request):
    form=QuestionForm(request.POST,request.FILES)
    if form.is_valid():
        new_question=form.save(commit=False)
        new_question.date=timezone.now()
        new_question.save()
        hashtag=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_question.hashtag.add(new_hashtag[0])
        return redirect('detail', new_question.id)
    return redirect('main')

def delete(request, question_id):
    question_delete=get_object_or_404(Question, pk=question_id)
    question_delete.delete()
    return redirect('main')

def update_page(request, question_id):
    question_update=get_object_or_404(Question,pk=question_id)
    return render(request, 'update.html', {'question':question_update})

def update(request, question_id):
    question_update = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        title = request.POST.get('title', '')  
        content = request.POST.get('content', '')  
        question_update.title = title
        question_update.content = content
        question_update.save()
        return redirect('main')
    else:
        return render(request, 'update.html', {'question': question_update})
    
def add_comment(request, question_id):
    community = get_object_or_404(Question,pk=question_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = community
            comment.save()
            return redirect('detail', question_id)
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form})

    
@login_required(login_url='/accounts/login')
def like(request,bid):
    # 어떤 게시물에, 어떤 사람이 like를 했는 지
    question = Question.objects.get(id=bid) # 게시물 번호 몇번인지 정보 가져옴
    user = request.user
    if question.like.filter(id=user.id).exists(): # 유저면 알아서 유저의 id로 검색해줌
        question.like.remove(user)
        like_count = question.like.count()
        return JsonResponse({'message': 'deleted', 'like_cnt':like_count})
    else:
        question.like.add(user) # post의 like에 현재유저의 정보를 넘김
        like_count = question.like.count()
        return JsonResponse({'message': 'added', 'like_cnt' : like_count})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')  # 로그인 성공 시 이동할 페이지
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

    
    
    
    