import os
from dotenv import load_dotenv

# Load environment variables once here
load_dotenv()


class Settings:
    APP_ENV: str = os.getenv("APP_ENV", "development")
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    def validate(self):
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required")


settings = Settings()