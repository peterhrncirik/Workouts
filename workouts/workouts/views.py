from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.db.models import Q
from .models import Exercise
from .forms import WorkoutForm
from .workout import generate_workout

# Messages for debugging
from django.contrib import messages

class HomePageView(View):
    
    def get(self, request):
        form = WorkoutForm()
        context = {'form': form}
        return render(request, 'pages/home.html', context)
    
    def post(self, request):
        
        form = WorkoutForm(request.POST)
        if form.is_valid():
            bodyparts = form.cleaned_data.get('bodyparts')
            equipments = form.cleaned_data.get('equipment')
            difficulty = form.cleaned_data.get('difficulty')[0]
            
            match difficulty:
                case 'beginner':
                    exercises = Exercise.objects.filter(equipment='kettlebell').exclude(difficulty='hard').exclude(difficulty='medium')
                case 'intermediate':
                    exercises = Exercise.objects.filter(equipment='kettlebell').exclude(difficulty='hard')
                case _:
                    exercises = Exercise.objects.filter(equipment='kettlebell')
                     
            # exercises = Exercise.objects.filter(Q(bodypart__in=bodyparts)&Q(equipment__in=equipments))
            exercises = Exercise.objects.filter(Q(equipment__in=equipments))

            # To si checkni aka je length of returned exercises

            # daj filter ze ak nie je exercise pre dany tool, nebude taka moznost na bodypart
            
            workout = generate_workout(difficulty, exercises)

            
            return render(request, 'pages/result.html', {'workout': workout})


class AboutPageView(TemplateView):
    template_name = "pages/about.html"