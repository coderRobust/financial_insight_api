import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_ENV = os.getenv("APP_ENV", "development")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    def as_dict(self):
        return {
            "APP_ENV": self.APP_ENV,
            "HOST": self.HOST,
            "PORT": self.PORT,
            "LOG_LEVEL": self.LOG_LEVEL,
        }


settings = Settings()