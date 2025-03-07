from app import db

class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    content = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Scenario {self.name}>'
