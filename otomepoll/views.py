from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import Choice, Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:6]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'otomepoll/index.html', context)
    

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'otomepoll/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'otomepoll/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
       
        return render(request, 'otomepoll/detail.html', {
            'question': question,
            'error_message': "But you didn't select anything!",
        })
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('otomepoll:results', args=(question.id,)))
    
   


