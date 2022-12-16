from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import Exercise
from .forms import WorkoutForm


class HomePageView(View):
    
    def get(self, request):
        form = WorkoutForm()
        context = {'form': form}
        return render(request, 'pages/home.html', context)
    
    def post(self, request):
        
        form = WorkoutForm(request.POST)
        if form.is_valid():
            bodyparts = form.cleaned_data.get('bodyparts')
            equipment = form.cleaned_data.get('equipment')
            target = form.cleaned_data.get('target')
            return render(request, 'pages/result.html', {'x': bodyparts, 'y': equipment, 'z': target})
        return render(request, 'pages/result.html', {'x': form})


class AboutPageView(TemplateView):
    template_name = "pages/about.html"