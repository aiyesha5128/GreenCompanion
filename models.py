from app import db

# Plant categories association table (many-to-many)
plant_categories = db.Table(
    'plant_categories',
    db.Column('plant_id', db.Integer, db.ForeignKey('plant.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Plant(db.Model):
    """Model for plant information"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    scientific_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    
    # Care information
    light_needs = db.Column(db.String(100), nullable=False)
    watering = db.Column(db.String(100), nullable=False)
    soil_type = db.Column(db.String(100), nullable=False)
    humidity = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.String(100), nullable=False)
    fertilizing = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    toxicity = db.Column(db.String(100), nullable=False)
    
    # Many-to-many relationship with categories
    categories = db.relationship('Category', secondary=plant_categories, 
                                lazy='subquery', backref=db.backref('plants', lazy=True))
    
    def __repr__(self):
        return f'<Plant {self.name}>'

class Category(db.Model):
    """Model for plant categories"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'
