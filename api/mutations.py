from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Post

# Resolver to add post to DB
@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, title, description): 
    try:
        today = date.today()
        # Create post object with provided info
        post = Post(
            title=title, description=description, created_at=today.strftime("%b-%d-%Y")
        )
        # Add post object to DB 
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload

# Resolver to update post in DB
@convert_kwargs_to_snake_case
def update_post_resolver(ob, info, id, title, description):
    try: 
        post = Post.query.get(id)
        # If post, change title and description
        if post:
           post.title = title
           post.description = description
        # Add updated post to database
        db.session.add(post)
        db.session.commit()
        payload = {
           "success": True,
           "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False, 
            "errors": ["item matching id {id} not found"]
        }
    return payload

# Resolver to remove post from DB
@convert_kwargs_to_snake_case
def delete_post_resolver(obj, info, id):
    try:
        # Get post
        post = Post.query.get(id)
        # Delete post from DB
        db.session.delete(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not Found"]
        }
    return payload
  