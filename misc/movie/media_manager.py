from media import Movie
import fresh_tomatoes

toy_story = Movie("Toy Story", "A boy's toys are alive, and secretly watching him.","https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = Movie("Avatar", "A marine on an alien plannet.", "https://i.ytimg.com/vi_webp/a0CDJZu4M5I/movieposter.webp","https://www.youtube.com/watch?v=5PSNL1qE6VY")


print(toy_story.storyline)
print(avatar.storyline)

#toy_story.show_trailer()

o_brother = Movie("O Brother, Where Art Thou", "In the deep south during the 1930s, three escaped convicts search for hidden treasure while a relentless lawman pursues them.","https://images-na.ssl-images-amazon.com/images/M/MV5BYmFhNjMwM2EtNGViMy00MTZmLWIzNTYtYzg1NWYwNTE2MGJhXkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=eW9Xo2HtlJI")

suburbicon = Movie("Suburbicon", "A home invasion rattles a quiet family town.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA3MjA1NDkxMTReQTJeQWpwZ15BbWU4MDU2Njg3NDMy._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=HegUiva5JzA")

all_i_see_is_you = Movie("All I See is You", "A blind woman's relationship with her husband changes when she regains her sight and discovers disturbing details about themselves.", "https://images-na.ssl-images-amazon.com/images/M/MV5BNDI5NzU2OTM1MV5BMl5BanBnXkFtZTgwNzU3NzM3MzI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=zTTaFg2Sq9Y")

movies = [o_brother,suburbicon,all_i_see_is_you,toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)