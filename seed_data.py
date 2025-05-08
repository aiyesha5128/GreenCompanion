import os
from app import app, db
from models import Plant, Category

def seed_categories():
    """Seed the database with plant categories"""
    categories = [
        {"name": "Low Light", "description": "Plants that thrive in low light conditions"},
        {"name": "Bright Light", "description": "Plants that prefer bright, indirect light"},
        {"name": "Direct Sun", "description": "Plants that can tolerate direct sunlight"},
        {"name": "Pet Friendly", "description": "Plants that are non-toxic to pets"},
        {"name": "Air Purifying", "description": "Plants known for their air-purifying qualities"},
        {"name": "Drought Tolerant", "description": "Plants that can withstand periods of drought"},
        {"name": "Humidity Loving", "description": "Plants that thrive in high humidity environments"},
        {"name": "Beginner Friendly", "description": "Easy-to-care-for plants ideal for beginners"},
        {"name": "Flowering", "description": "Plants that produce flowers"},
        {"name": "Trailing", "description": "Plants with trailing or cascading growth habit"}
    ]
    
    for category_data in categories:
        category = Category.query.filter_by(name=category_data["name"]).first()
        if not category:
            category = Category(**category_data)
            db.session.add(category)
    
    db.session.commit()
    print("Categories seeded successfully!")

def seed_plants():
    """Seed the database with plant information"""
    
    # First get all categories
    categories = {category.name: category for category in Category.query.all()}
    
    plants_data = [
        {
            "name": "Snake Plant",
            "scientific_name": "Sansevieria trifasciata",
            "description": "The Snake Plant is one of the most popular and hardy houseplants. Its architectural, sword-like leaves and ability to thrive on neglect make it perfect for beginners.",
            "image_url": "https://www.thespruce.com/thmb/qoFJ9KXHZs9es9hXKnITQxYtlMQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1268976296-e13c5a14690d4f50bf30c6d3216eb5a3.jpg",
            "light_needs": "Low to bright indirect",
            "watering": "Allow soil to dry completely between waterings",
            "soil_type": "Well-draining potting mix",
            "humidity": "Low to average",
            "temperature": "60-85°F (15-29°C)",
            "fertilizing": "Fertilize lightly 2-3 times during growing season",
            "difficulty": "Easy",
            "toxicity": "Mildly toxic to pets",
            "categories": ["Low Light", "Drought Tolerant", "Air Purifying", "Beginner Friendly"]
        },
        {
            "name": "Pothos",
            "scientific_name": "Epipremnum aureum",
            "description": "Pothos is a popular trailing vine with heart-shaped leaves that come in various patterns. It's extremely adaptable and can grow in a variety of conditions.",
            "image_url": "https://www.almanac.com/sites/default/files/styles/large/public/image_nodes/pothos_usmee_ss-crop.jpg",
            "light_needs": "Low to bright indirect",
            "watering": "Allow top inch of soil to dry between waterings",
            "soil_type": "Standard potting mix",
            "humidity": "Average",
            "temperature": "65-85°F (18-29°C)",
            "fertilizing": "Monthly during growing season",
            "difficulty": "Easy",
            "toxicity": "Toxic to pets",
            "categories": ["Low Light", "Trailing", "Air Purifying", "Beginner Friendly"]
        },
        {
            "name": "Spider Plant",
            "scientific_name": "Chlorophytum comosum",
            "description": "The Spider Plant is a classic, easy-to-grow houseplant that produces arching leaves and tiny plantlets that hang down like spiders on a web.",
            "image_url": "https://www.thespruce.com/thmb/Q3KF5H3pZGGx-78LbcGkap0EL4k=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/spider-plant-chlorophytum-definition-1902773-01-4fc579ee1b874560841e95f0520fa407.jpg",
            "light_needs": "Bright indirect",
            "watering": "Keep soil lightly moist",
            "soil_type": "Well-draining potting mix",
            "humidity": "Average",
            "temperature": "65-75°F (18-24°C)",
            "fertilizing": "Every 2-3 months during growing season",
            "difficulty": "Easy",
            "toxicity": "Non-toxic to pets and humans",
            "categories": ["Pet Friendly", "Air Purifying", "Beginner Friendly"]
        },
        {
            "name": "Peace Lily",
            "scientific_name": "Spathiphyllum",
            "description": "The Peace Lily is known for its dark leaves and contrasting white flowers. It's a popular choice for low-light environments and is excellent at indicating when it needs water by drooping.",
            "image_url": "https://www.thespruce.com/thmb/Mf4tMXDu3C1K3JAnacCJNvn6geo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/peace-lily-growing-conditions-1902767-05-5c06d2c346e0fb00012af913-7990422b9a0d473d92d4c41e4cb3cec2.jpg",
            "light_needs": "Low to medium indirect",
            "watering": "Keep soil lightly moist",
            "soil_type": "Rich, well-draining potting mix",
            "humidity": "High",
            "temperature": "65-85°F (18-29°C)",
            "fertilizing": "Every 6-8 weeks during growing season",
            "difficulty": "Easy",
            "toxicity": "Toxic to pets",
            "categories": ["Low Light", "Flowering", "Air Purifying", "Humidity Loving"]
        },
        {
            "name": "ZZ Plant",
            "scientific_name": "Zamioculcas zamiifolia",
            "description": "The ZZ Plant is prized for its glossy, dark green leaves and virtually indestructible nature. It can tolerate long periods of neglect and still look fantastic.",
            "image_url": "https://www.thespruce.com/thmb/TNsJzf_O8_azCiLNsIBXG3y5Coo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/zz-zanzibar-gem-plant-profile-4796783-02-8a9b9440a53a42d599d97c9ff16b8396.jpg",
            "light_needs": "Low to bright indirect",
            "watering": "Allow soil to dry completely between waterings",
            "soil_type": "Well-draining potting mix",
            "humidity": "Low to average",
            "temperature": "65-85°F (18-29°C)",
            "fertilizing": "Sparingly, 2-3 times per year",
            "difficulty": "Easy",
            "toxicity": "Toxic if ingested",
            "categories": ["Low Light", "Drought Tolerant", "Beginner Friendly"]
        },
        {
            "name": "Monstera",
            "scientific_name": "Monstera deliciosa",
            "description": "The Monstera is beloved for its dramatic, perforated leaves. Also known as the Swiss Cheese Plant, it makes a striking statement in any space as it grows.",
            "image_url": "https://www.thespruce.com/thmb/x80EEPn1iiT4atYwNPcB-px1UlE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/grow-monstera-adansonii-swiss-cheese-plant-1902774-hero-01-dc903dae459a4dd4807130ce04ab05a8.jpg",
            "light_needs": "Medium to bright indirect",
            "watering": "Allow top inch of soil to dry between waterings",
            "soil_type": "Rich, well-draining potting mix",
            "humidity": "Medium to high",
            "temperature": "65-85°F (18-29°C)",
            "fertilizing": "Monthly during growing season",
            "difficulty": "Moderate",
            "toxicity": "Toxic to pets",
            "categories": ["Humidity Loving", "Air Purifying"]
        },
        {
            "name": "Fiddle Leaf Fig",
            "scientific_name": "Ficus lyrata",
            "description": "The Fiddle Leaf Fig has become an interior design staple with its large, violin-shaped leaves. Though beautiful, it requires consistent care to thrive.",
            "image_url": "https://www.thespruce.com/thmb/FZ1i6t701U8Z7M9SZJEAHDTQqOE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/grow-fiddle-leaf-fig-tree-ficus-lyrata-1902756-04-13df25bf914d48648b397c67ef80a1ab.jpg",
            "light_needs": "Bright indirect",
            "watering": "Allow top few inches of soil to dry between waterings",
            "soil_type": "Well-draining potting mix",
            "humidity": "Medium to high",
            "temperature": "65-75°F (18-24°C)",
            "fertilizing": "Monthly during growing season",
            "difficulty": "Moderate to difficult",
            "toxicity": "Toxic to pets",
            "categories": ["Bright Light", "Humidity Loving"]
        },
        {
            "name": "Rubber Plant",
            "scientific_name": "Ficus elastica",
            "description": "The Rubber Plant features thick, glossy leaves in deep green, burgundy, or variegated patterns. It's more forgiving than many other ficuses and can grow into an impressive tree.",
            "image_url": "https://www.thespruce.com/thmb/3yrS5l-IMfuh2BQR74jy4Bg8UhA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1205145465-9d80783f49444f8b8c3eaa652a4ad8e3.jpg",
            "light_needs": "Medium to bright indirect",
            "watering": "Allow top few inches of soil to dry between waterings",
            "soil_type": "Well-draining potting mix",
            "humidity": "Average",
            "temperature": "60-80°F (15-27°C)",
            "fertilizing": "Monthly during growing season",
            "difficulty": "Moderate",
            "toxicity": "Toxic to pets",
            "categories": ["Air Purifying", "Bright Light"]
        },
        {
            "name": "Boston Fern",
            "scientific_name": "Nephrolepis exaltata",
            "description": "The Boston Fern is a classic houseplant with feathery, arching fronds. It adds a soft, lush touch to any space but requires attentive care to stay lush.",
            "image_url": "https://www.thespruce.com/thmb/B3sR2mFfPUC3_5H3LsNzQCCLnKM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/grow-boston-ferns-1902733-07-d9d8a72be80f415297a49131fa517fbb.jpg",
            "light_needs": "Medium indirect",
            "watering": "Keep soil consistently moist",
            "soil_type": "Rich, well-draining potting mix",
            "humidity": "High",
            "temperature": "65-75°F (18-24°C)",
            "fertilizing": "Monthly during growing season",
            "difficulty": "Moderate",
            "toxicity": "Non-toxic to pets and humans",
            "categories": ["Pet Friendly", "Humidity Loving", "Air Purifying"]
        },
        {
            "name": "Aloe Vera",
            "scientific_name": "Aloe barbadensis miller",
            "description": "Aloe Vera is a succulent plant known for its medicinal properties. Its thick, fleshy leaves contain a gel that can be used to soothe minor burns and skin irritations.",
            "image_url": "https://www.thespruce.com/thmb/1i4j0P_V9a-LslhafGTGSi6qnqk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/grow-aloe-vera-1902502-05-a724a2d4f13a4ce6a7d61637eadf3fee.jpg",
            "light_needs": "Bright indirect to direct",
            "watering": "Allow soil to dry completely between waterings",
            "soil_type": "Cactus or succulent mix",
            "humidity": "Low",
            "temperature": "65-85°F (18-29°C)",
            "fertilizing": "Sparingly, few times per year",
            "difficulty": "Easy",
            "toxicity": "Toxic to pets",
            "categories": ["Direct Sun", "Drought Tolerant", "Beginner Friendly"]
        },
    ]
    
    for plant_data in plants_data:
        # Extract and remove categories from plant data
        plant_categories = plant_data.pop('categories', [])
        
        # Check if plant already exists
        existing_plant = Plant.query.filter_by(name=plant_data["name"]).first()
        
        if not existing_plant:
            # Create new plant
            plant = Plant(**plant_data)
            
            # Add categories
            for category_name in plant_categories:
                if category_name in categories:
                    plant.categories.append(categories[category_name])
                
            db.session.add(plant)
    
    db.session.commit()
    print("Plants seeded successfully!")

if __name__ == '__main__':
    with app.app_context():
        # Create the database tables if they don't exist
        db.create_all()
        
        # Seed the database with categories and plants
        seed_categories()
        seed_plants()
