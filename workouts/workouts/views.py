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
            target = form.cleaned_data.get('target')
            difficulty = form.cleaned_data.get('difficulty')[0]
            
            # If user selects both bodypart and equipment
            if bodyparts and equipments:
                exercises = Exercise.objects.filter(Q(bodypart__in=bodyparts)&Q(equipment__in=equipments))
                messages.info(request, f'Both Bodyparts & Equipments')
                workout1 = workout(difficulty, exercises)
            # if user selects only bodypart
            elif bodyparts:
                exercises = Exercise.objects.filter(bodypart__in=bodyparts)
                messages.info(request, f'Only Bodyparts')
                workout1 = workout(difficulty, exercises)
            # if user selects only equipment
            elif equipments:
                exercises = Exercise.objects.filter(equipment__in=equipments)
                messages.info(request, f'Only equipments')
                workout = generate_workout(difficulty, exercises)
            
            return render(request, 'pages/result.html', {'x': bodyparts, 'y': equipments, 'z': target, 'e': exercises, 'd': difficulty, 'workout': workout})


class AboutPageView(TemplateView):
    template_name = "pages/about.html"