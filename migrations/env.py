from alembic import context
from sqlalchemy import engine_from_config, pool
import os

# Import all models
from shared.models.base import Base
from shared.models import health_logs

config = context.config

# Override database URL from environment
database_url = os.getenv('DATABASE_URL')
if database_url:
    config.set_main_option('sqlalchemy.url', database_url)

target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()