movies_dictionary = []

def add_movies():
    
    # Movie title 
    title = input(str("Please input movie title ? "))
    # Director 
    director = input(str("Please input name of director ? "))
    # Release year 
    release_year = input(str("Please input release year ? "))
    movies_dictionary.append({'title': title, 'director': director,'release_year' : release_year})
    

def view_movies():
    print(movies_dictionary)

def find_movies():
    movie_name = input(str("Type the name of the movie you are searching ? "))
    for i in movies_dictionary:
        if i['title'] == movie_name:
            print(i)



prompt = "Click 'a' to add movie, Click 'v' to view collection, Click 'f' to find movie by title and 'q' to quit "

def menu():
    user_input = input(prompt)
    while user_input != 'q':
        if user_input == 'a':
            add_movies()
        elif user_input == 'v':
            view_movies()
        elif user_input == 'f':
            find_movies()
        else: 
            print("wrong input, please choose options correctly")
        user_input = input(prompt)

menu()

