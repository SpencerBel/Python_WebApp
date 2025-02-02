from .models import Post
from ariadne import convert_kwargs_to_snake_case

# Resolver to fetch all Posts from DB
def listPosts_resolver(obj, info):
    try:
        # Retrieve all Posts 'Post' from the DB
        posts = [post.to_dict() for post in Post.query.all()]
        print(posts)
        # Success response
        payload = {
            "success": True,
            "posts": posts
        }
    # Exception handling 
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

# Resolver to fetch a Post by its ID
@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        # Retrieve post with "id" from DB
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    # Exception handling
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload