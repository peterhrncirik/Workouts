import random

"""
Module consisting of functions that build actual workout based on difficulty selected

"""

def generate_workout(difficulty, exercises):
    
    
    match difficulty:
        case 'beginner':
            return generate_beginner_workout(exercises)
        case 'intermediate':
            return generate_intermediate_workout(exercises)
        case 'advanced':
            return generate_advanced_workout(exercises)

    
                

def generate_beginner_workout(exercises):
    
    workout = []
    
    for exercise in random.sample(list(exercises), k=random.randint(2, 4)):
        
        workout.append({
            'img': exercise.cover_img,
            'name': exercise.name,
            'sets': random.randint(2, 3),
            'reps': random.randint(8, 12),
        })
    

    return workout


def generate_intermediate_workout(exercises):
    
    workout = []
    
    for exercise in random.sample(list(exercises), k=random.randint(3, 6)):
        
        workout.append({
            'img': exercise.cover_img,
            'name': exercise.name,
            'sets': random.randint(3, 5),
            'reps': random.randint(8, 16),
        })
    

    return workout

def generate_advanced_workout(exercises):
    
    workout = []
    
    for exercise in random.sample(list(exercises), k=random.randint(4, 7)):
        
        workout.append({
            'img': exercise.cover_img,
            'name': exercise.name,
            'sets': random.randint(3, 6),
            'reps': random.randint(8, 20),
        })
    

    return workout

