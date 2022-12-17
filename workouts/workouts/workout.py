import random

def generate_workout(difficulty, exercises):
    
    match difficulty:
        case 'beginner':
            return generate_beginner_workout(exercises)
        case 'intermediate':
            generate_intermediate_workout(exercises)
        case 'advanced':
            generate_advanced_workout(exercises)
        case 'finisher':
            generate_finisher_workout(exercises)
    
    
    # if difficulty == 'beginner':
    #     workout = {
    #         'sets': random.randint(2, 4),
    #         'reps': random.randint(250, 300),
    #         'rest': random.randint(5, 10),
    #         'exercises': random.sample([exercise.name for exercise in exercises], random.randint(2, 8)),
    #     }
    # elif difficulty == 'intermediate':
    #     workout = {
    #         'sets': random.randint(20, 30),
    #         'reps': random.randint(250, 300),
    #         'rest': random.randint(20, 30),
    #         'exercises': random.sample([exercise.name for exercise in exercises], random.randint(2, 8)),
    #     }
    # elif difficulty == 'advanced':
    #     workout = {
    #         'sets': random.randint(50, 70),
    #         'reps': random.randint(250, 300),
    #         'rest': random.randint(50, 70),
    #         'exercises': random.sample([exercise.name for exercise in exercises], random.randint(2, 8)),
    #     }
    # else:
    #     workout = {
    #         'sets': random.randint(100, 150),
    #         'reps': random.randint(250, 300),
    #         'rest': random.randint(100, 150),
    #         'exercises': random.sample([exercise.name for exercise in exercises], random.randint(2, 8)),
    #     }
    
    # return workout
                

def generate_beginner_workout(exercises):
    
    workout = {
            'sets': random.randint(2, 4),
            'reps': random.randint(250, 300),
            'rest': random.randint(5, 10),
            'exercises': random.sample([exercise.name for exercise in exercises], random.randint(2, 8)),
        }
    return workout


def generate_intermediate_workout(exercises):
    pass

def generate_advanced_workout(exercises):
    pass

def generate_finisher_workout(exercises):
    pass