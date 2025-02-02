from app import db

# Define Post model
class Post(db.Model):
    # Define fields in the DB table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)
    # Convert instance of Post into Python Dictionary (to serialize object to JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            # Converts created_at into string formatted as DD-MM-YY
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }
        