from flask import Blueprint, render_template, session, redirect
from app.models import Post
from app.db import get_db
from sqlalchemy import func
from app.models import Vote

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  # get all posts
  db = get_db()
  posts = (
    db.query(Post)
      .outerjoin(Vote, Vote.post_id == Post.id)
      .group_by(Post.id)
      .order_by(
        func.count(Vote.id).desc(),     # most upvotes first
        Post.created_at.desc()          # tie-breaker: newest first
      )
      .all()
)
  return render_template(
  'homepage.html',
  posts=posts,
  loggedIn=session.get('loggedIn')
)

@bp.route('/login')
def login():
  # not logged in yet
  if session.get('loggedIn') is None:
    return render_template('login.html')

  return redirect('/dashboard')

@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # render single post template
  return render_template(
  'single-post.html',
  post=post,
  loggedIn=session.get('loggedIn')
)