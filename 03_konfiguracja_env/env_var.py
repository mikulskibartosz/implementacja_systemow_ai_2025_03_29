import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/postgres")
API_KEY = os.getenv("API_KEY")

print(DATABASE_URL)
print(API_KEY)
