# spillthetea

This is mini social network project, built with python's Django framework, Vanilla JavaScript, Sass and is being deployed on Heroku. Spill the tea - Idea is that everyone can freely gossip and say any stupid(or smart) thing that comes to one's mind. 

**[You can visit live site here](https://spillthetea.herokuapp.com/)**


## Here are some key features of this project: 
- Registration, login
- Add posts
- Like / Unlike posts
- Follow / Unfollow other users
- See all posts posted by any registered user
- See posts only from the users you follow
- Edit and save your post
- Change profile picture

## Javascript usage:
- Show/Hide password 
![Show/Hide](https://ibb.co/zZV6bww)
- Fetching database to edit and save text of your post
![Edit and Save](https://user-images.githubusercontent.com/95188330/217940991-50353683-da0d-4e3a-85fa-68c99fa8b596.png)
- Updating Likes count and fetching that information to the database. Changes svg icon to blue variation 
![image](https://user-images.githubusercontent.com/95188330/217941453-8d27a323-5097-48f0-b249-d2ef3561571e.png)


#### Models:
## Unoredered
- User model, with default abstractuser fields + imagefield for profile picture
- Post model with creator(Foreign key to user), content and timestamp fields
- Follow model with follower and follow receiver fields, both are foreignkeys to user. 
- Likes model with post field(Foreign key to model Post) and likedby field(Foreignkey to user).


### This project is built with the Model-View-Controller (MVC) architectural style, which provides a clear separation of responsibilities between the data model, the user interface, and the control logic. To see logic behind the controller, you can read the python code in Views.py. Project's code is on the second branch named Master. Thanks for your time!


