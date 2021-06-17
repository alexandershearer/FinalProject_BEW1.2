
# Gamer Hub

This project was designed to let gamers post and talk about games they are excited for or even
the games they are currently playing through. It will let you comment and give feedback to whoever
posts on the site.


## Authors

- [@alexandershearer](https://www.github.com/alexandershearer)

  
## Documentation

A few snippets of code will be here to share some of things going on in the background.

```
class GameForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=30)])
    body = StringField('Body', validators=[DataRequired(), Length(min=1, max=280)])
    image = StringField('Image', validators=[DataRequired(), url()])
    submit = SubmitField('Share')
```

This form is your primary post. It will allow you to give your post a title to give a 
quick overview of what your post is about. It also allows a body to give a description of
whatever you are posting. you will also be required to give an image URL to share with your
post for visual pleasure. Lastly you have your submit button to publish it to the site.


```
class ReplyForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired(), Length(min=1, max=280)])
    submit = SubmitField('Reply')
```
Here is a simply reply form to each post where you have just a body for what your reply will be
and a submit button to publish your comment to that post.
  
## Screenshots

![Login Picture](https://i.imgur.com/9ENQ6bm.png)

This is the first step when getting onto the site. You will be required to make an account
when you first try to post or even view any of the posts on the site. It only requires a username
and a password. **Usernames are unique and cannot be be reused.**
