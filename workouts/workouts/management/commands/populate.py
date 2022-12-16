from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from workouts.models import Exercise

class Command(BaseCommand):
    # Show this when the user types help
    help = "Import exercises into DB"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Exercise.objects.exists():
            print('Exercises already loaded into DB.')
            return
            
        # Show this before loading the data into the database
        print("Loading data")


        # Code to load the data into database
        for row in DictReader(open('./fitness_exercises.csv')):
            exercise=Exercise(name=row['name'], bodypart=row['bodyPart'], equipment=row['equipment'], image_url=row['gifUrl'], target=row['target'])  
            exercise.save()
            
        print('DONE')