import os
import secrets
from flask import render_template, url_for, redirect, request
from flask_blog1 import app, db
from flask_blog1.forms import PostForm
from flask_blog1.models import Post


# posts = [
#     {
#         'title': 'Post 1',
#         'description': 'Post1 description'
#     },
#     {
#         'title': 'Post 2',
#         'description': 'Post2 description'
#     },
# ]

# her iki route eyni yeri acir
@app.route("/")
@app.route("/home")
def home_page():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, description=form.description.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('add_post.html', form=form)




