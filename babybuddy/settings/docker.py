from .base import *

# Database - reads from environment variables set in docker-compose
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE") or "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME") or "postgres",
        "USER": os.getenv("DB_USER") or "postgres",
        "PASSWORD": os.environ.get("DB_PASSWORD") or os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.getenv("DB_HOST") or "db",
        "PORT": os.getenv("DB_PORT") or 5432,
    }
}

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, "../data/media")

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, "../static")
