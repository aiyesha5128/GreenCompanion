# PlantPal - Houseplant Identification & Care Guide

PlantPal is a web-based application that helps users identify common houseplants and provides detailed care instructions. The application focuses on 50-100 common houseplants with comprehensive care tips.

## Features

- **Plant Identification**: Search for plants by name, scientific name, or description
- **Detailed Care Information**: Each plant comes with specific care instructions including:
  - Light requirements
  - Watering schedule
  - Soil type recommendations
  - Humidity needs
  - Temperature preferences
  - Fertilizing guidelines
  - Difficulty level
  - Toxicity information

- **Filtering System**: Find plants that match your specific needs:
  - Light conditions (low light, bright indirect, direct sun)
  - Experience level (beginner, intermediate, advanced)
  - Pet friendliness (toxic vs non-toxic)

- **Categorized Browsing**: Browse plants by categories such as:
  - Low Light
  - Pet Friendly
  - Air Purifying
  - Drought Tolerant
  - And more

## Technology Stack

- **Backend**: Python with Flask framework
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **CSS Framework**: Bootstrap (Replit dark theme)
- **Icons**: Font Awesome

## Getting Started

### Prerequisites

- Python 3.11
- PostgreSQL database

### Installation

1. Clone the repository:
```
git clone <repository-url>
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Set up the environment variables:
```
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
SESSION_SECRET=<your-secret-key>
```

4. Initialize the database with seed data:
```
python seed_data.py
```

5. Run the application:
```
python main.py
```

The application will be available at `http://localhost:5000`.

## Database Schema

The application uses two main models:

1. **Plant**: Stores information about individual plants
   - Basic details (name, scientific name, description, image URL)
   - Care information (light, water, soil, etc.)
   - Difficulty and toxicity

2. **Category**: Represents plant categories
   - Name and description
   - Many-to-many relationship with plants

## Project Structure

- `app.py`: Flask application configuration
- `main.py`: Application entry point
- `models.py`: Database models (Plant, Category)
- `routes.py`: Route definitions for all pages
- `seed_data.py`: Script to populate the database with initial plant data
- `static/`: Static assets (CSS, JavaScript, images)
- `templates/`: HTML templates for all pages

## Future Enhancements

- User accounts for saving favorite plants
- Plant problem diagnosis
- Watering reminder functionality
- Plant growth tracking
- Community plant care tips
- Image-based plant identification

## License

This project is licensed under the MIT License - see the LICENSE file for details.