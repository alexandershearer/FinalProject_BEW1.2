from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime

from app.models import Post, Reply
from app.main.forms import PostForm, ReplyForm

from app import app, db


main = Blueprint('main', __name__)

# Create your routes here.

@main.route('/')
def homepage():
    all_posts = Post.query.all()
    return render_template('homepage.html', posts=all_posts)

@main.route('/make_post', methods=['GET', 'POST'])
@login_required
def make_post():
    form = PostForm()

    if form.validate_on_submit()
        post = Post(
            body=form.body.data,
            publish_date=date.today(),
            user=current_user
        )

        db.session.add(post)
        db.session.commit()

        flash('Your post was made successfully!')
        return redirect(url_for('main.homepage'))
    return render_template('make_post.html', form=form)

@main.route('/post/<post_id>')
@login_required
def post_detail(post_id):
    form = ReplyForm()
    post = Post.query.get(post_id)
    replies = Reply.query.filter_by(post_id=post_id)

    return render_template('post.html', post=post, replies=replies, form=form)


@main.route('/post/<post_id>')
@login_required
def post_reply(post_id):
    form = ReplyForm()
    post = Post.query.get(post_id)

    if form.validate_on_submit():
        reply = Reply(
            body=form.body.data,
            publish_date=date.today(),
            user=current_user,
            post=post
        )

        db.session.add(reply)
        db.session.commit()

        flash('Your reply was made successfully!')
        return redirect(url_for('main.post_detail', post_id=post_id))

    return render_template('post.html', form=form, post=post)