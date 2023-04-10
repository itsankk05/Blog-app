# Blog-app

#### Description:

Blog-app is a basic blogging application which allows users to create, update and delete their posts as well as view other users posts and comment on them. Users can also view other user's profile by clicking on their username. Every user needs to create a username while signing up for the app. The app takes the user's email and password to generate an account.

**App.py:**
This is the file which is executed in order to run the whole website.

**Models.py:**
This is the python file using SQLAlchemy through which I created all the necessary tables for the application, including their name, type, size etc.
There are mainly 4 tables in this project

**Views.py**
This is the pythoon file in which all the views are stored that is, it is the file where all the backend processing is done regarding the app. This file is responsible for all the processing i.e. the deletion of posts, increment of likes, adding of comments, checking whether the user is logged in or not or creating a post. Hence it manages the entire backend flow of the application

**Auth.py:**
This is the python file where all the authentication process is carried out. This is the file which is responsible for signing up users, logging them in and out. It also checks whether the user trying to signup already exists or not.

**init.py:**
This python file is required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as string , unintentionally hiding valid modules that occur later on the module search path.

**base.html**
This is the base template of our webpage. It contains the basic structure of how the webpage should look. It contains all the stylesheet links and javascript links. It is the basic template which is used by all other html files.

**create_post.html:**
This html file is the page we see when we click on the "create post" button on the homepage. It include the post body and the post button

**home.html:**
This is the home page of our website. This the page which is rendered when the user is signed up. It displays all the posts made by different users and you can insteract with those posts.

**Login.html:**
This is the login page of the website. It includes a simple form which asks the user his email and password.

**sign-up.html:**
This is the signup page of the website. It also includes a basic form which asks the user his username, email and asks him to setup a password. This all information is then sent to the database where it is then stored.

**posts-div.html**
This is the file which decides the layout of the posts that the user makes. This file displays the posts, displays the comments, deletes the commemnts, manages the "view comment button", displays the time and date of each comment, manages the likes on the post and links the users profile to his posts.

**posts.html:**
This is the html document which is rendered when a user clicks on another users profile. This file displays the profile of the user along with all the posts he has made.

**index.js:**
This is a javascript file which handles the likes on a post. It prevents the reloading of the whole page when liking or disliking a post.
