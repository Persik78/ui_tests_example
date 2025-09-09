import os

class Environment:
    BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8080")
    VALID_USERNAME = os.getenv("VALID_USERNAME", "Admin")
    VALID_PASSWORD = os.getenv("VALID_PASSWORD", "Admin123")