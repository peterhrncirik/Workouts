import random
        

def generate_workout(difficulty, exercises):
    
    match difficulty:
        case 'beginner':
            return generate_beginner_workout(exercises)
        case 'intermediate':
            return generate_intermediate_workout(exercises)
        case 'advanced':
            return generate_advanced_workout(exercises)
        case 'finisher':
            return generate_finisher_workout(exercises)
    
                

def generate_beginner_workout(exercises):
    
    workout = []
    
    for exercise in random.sample(list(exercises), k=5):
        
        workout.append({
            'img': exercise.cover_img,
            'name': exercise.name,
            'sets': random.randint(2, 4),
            'reps': random.randint(8, 12),
        })
    

    return workout


def generate_intermediate_workout(exercises):
    
    workout = []
    
    for exercise in random.sample(list(exercises), k=5):
        
        workout.append({
            'img': exercise.cover_img,
            'name': exercise.name,
            'sets': random.randint(2, 4),
            'reps': random.randint(8, 12),
        })
    

    return workout

def generate_advanced_workout(exercises):
    
    workout = []
    
    for exercise in random.sample(list(exercises), k=5):
        
        workout.append({
            'img': exercise.cover_img,
            'name': exercise.name,
            'sets': random.randint(2, 4),
            'reps': random.randint(8, 12),
        })
    

    return workout

def generate_finisher_workout(exercises):
   
    workout = []
    
    for exercise in exercises[:5]:
        
        workout.append(f'{exercise.name} {random.randint(2, 4)}x{random.randint(8, 12)}')
    

    return workout