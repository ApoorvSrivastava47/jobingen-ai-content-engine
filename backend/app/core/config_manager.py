from app.config.config import Config
from loguru import logger


class ConfigManager:
    @staticmethod
    def validate():
        logger.info("Validating configuration...")

        if not Config.DEFAULT_MODEL:
            raise ValueError("Default model is missing.")

        if Config.TEMPERATURE < 0 or Config.TEMPERATURE > 2:
            raise ValueError("Temperature must be between 0 and 2.")

        logger.success("Configuration validated successfully.")

    @staticmethod
    def get():
        ConfigManager.validate()
        return Config
