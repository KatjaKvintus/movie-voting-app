from repositories.MovieRepository import Movie_Repository



class Movie_Service:


    
    # Reads votes.txt file, counts votes for each movie, empties the file
    # and return the name of the winning movie.
    def count_votes():

        final_votes = {}

        with open("repositories/votes.txt") as file:
            for row in file:
                if row not in final_votes:
                    final_votes[row] = 0
                final_votes[row] = final_votes[row] +1
            file.close()

        most_votes = 0
        movie_with_most_votes = ""

        if final_votes:
            for movie in final_votes:
                if final_votes[movie] > most_votes:
                    most_votes = final_votes[movie]
                    movie_with_most_votes = movie

        result = movie_with_most_votes
        return result


    # For admin: check movie voting status
    def check_voting_list_status():

        top_movie = Movie_Service.count_votes()
        print(f"The movie with most votes right now is {top_movie}.")
        choice = input("Do you want to close woting and announce the winner? [Y]es or [N]o: ")

        if choice in ("Y", "y"):
            Movie_Repository.empty_voting_list()
            Movie_Repository.clear_all_votes()
            Movie_Repository.set_voting_status_message_as_winner_movie(top_movie)
        elif choice in ("N", "n"):
            print("Remember to close the voting in time before movie night.\n")

    # Prints a list of movies if it is available. If not available, it tells user to
    # try again later.
    def print_voting_list():

        if len(Movie_Repository.list_of_movies_to_be_voted) == 0:
            print("Unfortunatelyt the movie list is empty." 
            + "Come back later to check it again.\n")
        else:
            counter = 1
            print("The movie list for this weeks vote is: ")

            for movie in Movie_Repository.list_of_movies_to_be_voted:
                candidate_description = movie.movie_to_string() 
                print(f"[{counter}]: {candidate_description}")
                counter += 1
            print("")
    

   