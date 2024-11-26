from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class for storing settings."""
    REDIS_HOST: str
    REDIS_PORT: int
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')    

    @property
    def redis_url(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"
    
    
settings = Settings()