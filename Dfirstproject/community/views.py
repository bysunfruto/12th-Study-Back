from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import Question
from .forms import QuestionForm


# Create your views here.

def List(request):
    questions = Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'home.html', {'questions':questions})

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'detail.html', {'question':question})

def new(request):
    form=QuestionForm()
    return render(request, 'new.html',{'form':form})

def create(request):
    form=QuestionForm(request.POST,request.FILES)
    if form.is_valid():
        new_question=form.save(commit=False)
        new_question.date=timezone.now()
        new_question.save()
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
    
    
    
    