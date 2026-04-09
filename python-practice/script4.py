import os

env = os.getenv("APP_ENV", "prod")
print(f"Environment: {env}")