from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from api.queries import listPosts_resolver, getPost_resolver
from api.mutations import create_post_resolver, update_post_resolver, delete_post_resolver

# Create new graphql object 'query' 
query = ObjectType("Query")
# Create a new graphql object 'mutation
mutation = ObjectType("Mutation")

# Attach resolvers to queries 
query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)
mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)


# Load graphql schema
type_defs = load_schema_from_path("schema.graphql")
# Combine loaded schema with resolvers to create executable Graphql schema
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

# Route decorator 
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return ExplorerGraphiQL().html(None), 200

# Route decorator
@app.route("/graphql", methods=["POST"])
def graphql_server():
    # Extract json from incoming HTTP request
    data = request.get_json()
    # Execute grapql/query synchronously 
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    # Return result as JSON
    return jsonify(result), status_code





