from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):

        for user in self.users_collection:
            if user.username == username:
                break
        else:
            raise Exception("This user does not exist!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            if k == "title":
                movie.title = v
            elif k == "year":
                movie.year = v
            elif k == "age_restriction":
                movie.age_restriction = v
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.remove(movie)
                break
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        for user in self.users_collection:
            if user.username == username:
                if movie in user.movies_owned:
                    raise Exception(f"{username} is the owner of the movie {movie.title}!")
                if movie in user.movies_liked:
                    raise Exception(f"{username} already liked the movie {movie.title}!")

                user.movies_liked.append(movie)
                movie.likes += 1
                return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        for user in self.users_collection:
            if user.username == username:
                if movie not in user.movies_liked:
                    raise Exception(f"{username} has not liked the movie {movie.title}!")

                user.movies_liked.remove(movie)
                movie.likes -= 1
                return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        res = []
        for movie in sorted(self.movies_collection, key=lambda x: [-x.year, x.title]):
            res.append(movie.details())

        return "\n".join(res)

    def __str__(self):
        res = []
        if not self.users_collection:
            res.append("All users: No users.")
        else:
            hi = [user.username for user in self.users_collection]
            res.append(f"All users: {', '.join(hi)}")

        if not self.movies_collection:
            res.append("All movies: No movies.")
        else:
            bye = [movie.title for movie in self.movies_collection]
            res.append(f"All movies: {', '.join(bye)}")
        return "\n".join(res)
