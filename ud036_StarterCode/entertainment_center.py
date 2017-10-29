import media
import fresh_tomatoes

# wrapping the job of making a  list of movies into a function.
# this function statically builds an array of movies, and returns them.
def make_list_of_movies():
    ''' this function statically builds Movies() objects,
        and returns an array of the Movie() objects '''

    avatar = media.Movie("Avatar", "Like Minecraft and Alien combined",\
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg", \
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
    suburbicon = media.Movie("Suburbicon", "A home invasion rattles a quiet family town.", \
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA3MjA1NDkxMTReQTJeQWpwZ15BbWU4MDU2Njg3NDMy._V1_UX182_CR0,0,182,268_AL_.jpg", \
        "https://www.youtube.com/watch?v=HegUiva5JzA")
    all_i_see_is_you = media.Movie("All I See is You", \
        "A blind woman's relationship with her husband changes when she regains her sight and discovers disturbing details about themselves.", \
        "https://images-na.ssl-images-amazon.com/images/M/MV5BNDI5NzU2OTM1MV5BMl5BanBnXkFtZTgwNzU3NzM3MzI@._V1_UX182_CR0,0,182,268_AL_.jpg", \
        "https://www.youtube.com/watch?v=zTTaFg2Sq9Y")
    toy_story = media.Movie("Toy Story", "A boy's toys are alive, and secretly watching him.", \
        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", \
        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    crooklyn = media.Movie("Crooklyn", "Make yourself at home with the Carmichael family as they \
        experience one very special summer in their Brooklyn neighborhood that they've affectionately \
        nicknamed 'Crooklyn'.", \
        "https://images-na.ssl-images-amazon.com/images/M/MV5BYWEyM2Q3NDktM2E2Ni00OWIyLWIyYmItMWEyOGRmN2FkZjQ3XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg", \
        "http://www.youtube.com/watch?v=M4ivoM-19yA")
    o_brother = media.Movie("O Brother, Where Art Thou", \
        "In the deep south during the 1930s, three escaped convicts search for hidden treasure while a relentless lawman pursues them.", \
        "https://images-na.ssl-images-amazon.com/images/M/MV5BYmFhNjMwM2EtNGViMy00MTZmLWIzNTYtYzg1NWYwNTE2MGJhXkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_UX182_CR0,0,182,268_AL_.jpg", \
        "https://www.youtube.com/watch?v=eW9Xo2HtlJI")
 
    return [crooklyn, o_brother, avatar, suburbicon, all_i_see_is_you, toy_story]


def main():
    '''Main program to run automatically when this module is called directly'''
    movies_list = make_list_of_movies()
    for movie in movies_list:
        print(movie.getmoviesummaries(movie))
    fresh_tomatoes.open_movies_page(movies_list)


if __name__ == '__main__':
    main()
