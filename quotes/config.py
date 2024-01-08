from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str = 'django-insecure-whl7g6agx@)1d$7#nt91gdvm*z^!33*d)y2@c*6)t7%-p%_)ql'
    db_name: str = 'djangoDB'
    db_host: str = '127.0.0.1'
    db_port: int = 5432
    db_user: str = 'postgres'
    db_password: int = 1231
    email_host: str = 'smtp.meta.ua'
    email_port: int = 465
    email_starttls: bool = False
    email_use_ssl: bool = True
    email_use_tls: bool = False
    email_host_user: str = 'example@example.com'
    email_host_password: str = '1231'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()