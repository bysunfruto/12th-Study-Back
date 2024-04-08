from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import Question
from .Forms import QuestionForm

# Create your views here.

def list(request):
    posts = Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Question, pk=pk)
    return render(request, 'detail.html', {'post':post})

def new(request):
    form=QuestionForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form=QuestionForm(request.POST, request.FILES)
    if form.is_valid():
        new_question=form.save(commit=False)
        new_question.upload_time=timezone.now()
        new_question.save()
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
