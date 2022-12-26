from django import forms
from .models import Exercise
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class WorkoutForm(forms.Form):
    
    BODYPART_CHOICES = (
        ('back', 'back'),
        ('cardio', 'cardio'),
        ('chest', 'chest'),
        ('lower arms', 'lower arms'),
        ('lower legs', 'lower legs'),
        ('neck', 'neck'),
        ('shoulders', 'shoulders'),
        ('upper arms', 'upper arms'),
        ('upper legs', 'upper legs'),
        ('waist', 'waist'),
    )
    
    EQUIPMENT_CHOICES = (
        # ('body weight', 'body weight'),
        # ('cable', 'cable'),
        # ('leverage machine', 'leverage machine'),
        # ('assisted', 'assisted'),
        # ('medicine ball', 'medicine ball'),
        # ('stability ball', 'stability ball'),
        # ('band', 'band'),
        # ('barbell', 'barbell'),
        # ('rope', 'rope'),
        # ('dumbbell', 'dumbbell'),
        # ('ez barbell', 'ez barbell'),
        # ('sled machine', 'sled machine'),
        # ('upper body ergometer', 'upper body ergometer'),
        ('kettlebell', 'Kettlebell'),
        # ('olympic barbell', 'olympic barbell'),
        # ('weighted', 'weighted'),
        # ('bosu ball', 'bosu ball'),
        # ('resistance band', 'resistance band'),
        # ('roller', 'roller'),
        # ('skierg machine', 'skierg machine'),
        # ('hammer', 'hammer'),
        # ('smith machine', 'smith machine'),
        # ('wheel roller', 'wheel roller'),
        # ('stationary bike', 'stationary bike'),
        # ('tire', 'tire'),
        # ('trap bar', 'trap bar'),
        # ('elliptical machine', 'elliptical machine'),
        # ('stepmill machine', 'stepmill machine'),
    )
    
    TARGET_CHOICES = (
        ('abs', 'abs'),    
        ('quads', 'quads'),
        ('lats', 'lats'),  
        ('calves', 'calves'),
        ('pectorals', 'pectorals'),
        ('glutes', 'glutes'),
        ('hamstrings', 'hamstrings'),
        ('adductors', 'adductors'),
        ('triceps', 'triceps'),
        ('cardiovascular system', 'cardiovascular system'),
        ('spine', 'spine'),
        ('upper back', 'upper back'),
        ('biceps', 'biceps'),
        ('delts', 'delts'),
        ('forearms', 'forearms'),
        ('traps', 'traps'),
        ('serratus anterior', 'serratus anterior'),
        ('abductors', 'abductors'),
        ('levator scapulae', 'levator scapulae'),
    )
    
    DIFFICULTY_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', "I'm ready!", css_class="btn btn-danger"))

    
    equipment = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        choices=EQUIPMENT_CHOICES, 
        label='Equipment: ',
        required=False
    )
    
    difficulty = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        choices=DIFFICULTY_CHOICES, 
        label='Difficulty: ',
        required=False
    )
    



    