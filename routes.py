from flask import render_template, request, redirect, url_for, flash
from sqlalchemy import or_
from app import app, db
from models import Plant, Category

@app.route('/')
def index():
    """Home page with featured plants"""
    featured_plants = Plant.query.limit(6).all()
    categories = Category.query.all()
    return render_template('index.html', 
                          featured_plants=featured_plants, 
                          categories=categories)

@app.route('/plant/<int:plant_id>')
def plant_detail(plant_id):
    """Individual plant detail page"""
    plant = Plant.query.get_or_404(plant_id)
    # Get recommended plants from the same categories
    recommended_plants = []
    for category in plant.categories:
        for related_plant in category.plants:
            if related_plant.id != plant.id and related_plant not in recommended_plants:
                recommended_plants.append(related_plant)
                if len(recommended_plants) >= 3:
                    break
        if len(recommended_plants) >= 3:
            break
    
    return render_template('plant_detail.html', 
                          plant=plant, 
                          recommended_plants=recommended_plants[:3])

@app.route('/search')
def search():
    """Search for plants by name or characteristics"""
    query = request.args.get('query', '')
    if not query:
        return redirect(url_for('index'))
    
    # Search in name, scientific_name, and description
    results = Plant.query.filter(
        or_(
            Plant.name.ilike(f'%{query}%'),
            Plant.scientific_name.ilike(f'%{query}%'),
            Plant.description.ilike(f'%{query}%')
        )
    ).all()
    
    return render_template('search_results.html', 
                          results=results, 
                          query=query)

@app.route('/categories')
def all_categories():
    """View all plant categories"""
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@app.route('/category/<int:category_id>')
def category_detail(category_id):
    """View plants in a specific category"""
    category = Category.query.get_or_404(category_id)
    return render_template('search_results.html', 
                          results=category.plants, 
                          query=f'Category: {category.name}')

@app.route('/filter')
def filter_plants():
    """Filter plants by multiple criteria"""
    light = request.args.get('light')
    difficulty = request.args.get('difficulty')
    toxicity = request.args.get('toxicity')
    
    query = Plant.query
    
    if light:
        query = query.filter(Plant.light_needs == light)
    if difficulty:
        query = query.filter(Plant.difficulty == difficulty)
    if toxicity:
        query = query.filter(Plant.toxicity == toxicity)
    
    results = query.all()
    filter_description = []
    if light:
        filter_description.append(f"Light: {light}")
    if difficulty:
        filter_description.append(f"Difficulty: {difficulty}")
    if toxicity:
        filter_description.append(f"Toxicity: {toxicity}")
    
    filter_text = ", ".join(filter_description) if filter_description else "All Plants"
    
    return render_template('search_results.html', 
                          results=results, 
                          query=f'Filtered by: {filter_text}')

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 page"""
    return render_template('not_found.html'), 404
