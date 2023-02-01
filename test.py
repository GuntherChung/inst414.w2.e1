import json


with open ("imdb_movies_1985to2022.json", "r") as in_file:
    
    for line in in_file:
        print(line)
        this_movie = json.loads(line)
        
        actors = this_movie["actors"]
        for actor in actors:
            actor_name = actor[0]
            if actor_name == ['nm0413168', 'Hugh Jackman']:
                print("/t",actor_name)
                

