import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Print environment variables to verify they're loaded
print(f"DATABASE_URL: {os.environ.get('DATABASE_URL')}")
print(f"SESSION_SECRET: {os.environ.get('SESSION_SECRET')}")
