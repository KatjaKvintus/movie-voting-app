from entities.Movie import Movie


class AppUser:

    # Dictionary to store all users: username as the key and password as the value
    all_users = {}

    taken_usernames = []


    # The class constructor for creating new users
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.has_voted = False


    def create_new_user():

        username = input("Choose username (min. 3 characters long:) ")
        
        username_is_unique = AppUser.check_if_username_is_unique(username)
        username_is_long_enough = AppUser.check_username_length(username_is_unique)
        username = username_is_long_enough
        
        password = input("Choose password (min. 3 characters long): ")
        password_is_long_enough = AppUser.check_password_lenght(password)
        password = password_is_long_enough 

        AppUser.all_users[username] = password

        # Read file and save users to all_users dictionary
        with open("movieapp_users.txt", "a") as file:
            file.write(username + "," + password)
            file.write("\n")
            file.close()
        
        print("")
        print(f"Welcome to the movieapp, {username}!\n")
        Movie.welcome_to_movieapp()
    
    
    # Check returning users username and password
    def log_in_returning_user():

        username = input("What is your username? ")
        
        # Check is username exists
        username_exists = False
        while True:

            if username_exists:
                break

            if username not in AppUser.all_users.keys():
                print("I don't recognize this username. ")
                username = input("Please give correct username: ")
            
            if username in AppUser.all_users.keys():
                break
        
        # Ask for a password and check if those match. If not, keep asking password. 
        password = input("What is your password? ")

        if AppUser.all_users[username] != password:
            password_is_correct = False

            while True:
                if password_is_correct:
                    break

                print("Incorrect password. Please try again. \n")
                password = input("Password: ")

                if AppUser.all_users[username] == password:
                    password_is_correct = True  
        
        print(f"Welcome to Movie voting app, {username}!\n")
        Movie.welcome_to_movieapp()


    def check_if_username_is_unique(username):
        
        username_is_unique = False

        while True:

            if username_is_unique:
                break

            if username in AppUser.taken_usernames:
                print("This username is already taken.")
                username = input("Please choose unique username: ")
            
            if username not in AppUser.taken_usernames:
                username_is_unique = True
                return username


    def check_username_length(username):
        while True:
            if len(username) >= 3:
                return username
            else:
                print("You chose too short username. It should be at least 3 characters long.")
                username = input("Please choose longer username: ")


    def check_password_lenght(password):
        while True:
            if len(password) >= 3:
                return password
            else:
                print("You chose too short password. It should be at least 3 characters long.")
                password = input("Please choose longer username: ")

