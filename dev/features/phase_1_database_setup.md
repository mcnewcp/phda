# Feature 2: Database Setup

## Overview
Establish the PostgreSQL database foundation for the Personal Health Data Assistant (PHDA) project. This feature creates the core database schema, connection utilities, and migration system that will store all health data logged by users through the AI agent.

## Purpose
- Set up containerized PostgreSQL database with proper configuration
- Create SQLAlchemy models for core health data entities
- Establish Alembic migration system for schema versioning
- Implement database connection utilities with user isolation
- Provide the data persistence layer for all Phase 1 logging functionality

## Key Requirements

### Database Configuration
- **Database**: PostgreSQL 15+ in Docker container
- **User Isolation**: All tables include `user_id TEXT NOT NULL DEFAULT 'mcnewcp'`
- **Primary Keys**: All tables use `id SERIAL PRIMARY KEY` unless specified otherwise
- **Migrations**: Alembic-managed schema versioning
- **Connection**: Async-first with SQLAlchemy 2.0+ and asyncpg

### Core Health Data Models
Must support logging of these specific health data types through the AI agent:

1. **heart_log** - Heart rate and blood pressure measurements
2. **body_log** - Body composition metrics (weight, muscle mass, body fat)
3. **nutrition_log** - Food intake with nutritional information
4. **caffeine_log** - Caffeine consumption tracking
5. **alcohol_log** - Alcohol consumption tracking
6. **sauna_log** - Sauna session duration tracking

## Detailed Requirements

### 1. Docker PostgreSQL Configuration
- Container with PostgreSQL 15-alpine
- Named volume for data persistence
- Health check configuration
- Initialization script for database setup
- Environment variables from `.env` file

### 2. SQLAlchemy Models Structure
Each health model should follow this pattern with the specific schema:

**heart_log table:**
- datetime (timestamp): the datetime of the measurement
- systolic_mmhg (int): systolic pressure measurement
- diastolic_mmhg (int): diastolic pressure measurement
- rate_bpm (int): heart rate measurement

**body_log table:**
- datetime (timestamp): the datetime of the measurement
- weight_lb (float): body weight in lbs
- smm_lb (float): skeletal muscle mass in lbs
- pbf (float): percent body fat, in decimal form, e.g. 0.14
- ecw_tcw (float): extracellular water to total body water ratio in decimal format, e.g. 0.4

**nutrition_log table:**
- datetime (timestamp): the datetime of the food consumption
- short_description (str): A brief one-line description of the food item
- protein_g (float): Amount of protein in grams
- sodium_mg (float): Amount of sodium in milligrams
- potassium_mg (float): Amount of potassium in milligrams
- long_description (str): A detailed description of the food item with context

**caffeine_log table:**
- datetime (timestamp): the datetime of the measurement
- item_description (str): a short, couple word description of the item being logged, e.g. "green tea"
- caffeine_mg (float): the amount of caffeine in mg

**alcohol_log table:**
- datetime (timestamp): the datetime of the measurement
- item_description (str): a short, couple word description of the item being logged, e.g. "pint of beer"
- alcohol_oz (float): the amount of alcohol consumed, in ounces

**sauna_log table:**
- datetime (timestamp): the datetime of the measurement
- duration_min (int): the amount of time spent in the sauna in minutes

```python
class HealthLog(Base):
    """Base class for all health log tables."""
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(50), default='mcnewcp')
    datetime: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

class HeartLog(HealthLog):
    __tablename__ = 'heart_log'
    
    systolic_mmhg: Mapped[int] = mapped_column(Integer, nullable=False)
    diastolic_mmhg: Mapped[int] = mapped_column(Integer, nullable=False)
    rate_bpm: Mapped[int] = mapped_column(Integer, nullable=False)
    # ... additional constraints and indexes
```

### 3. Database Connection Management
- Async session factory using SQLAlchemy 2.0+
- Context manager for session handling
- Connection pooling configuration
- Environment-based database URL configuration

### 4. Alembic Migration System
- Complete Alembic configuration in `shared/db/migrations/`
- Environment configuration for async operations
- Automatic model detection for migrations
- Migration commands integration

### 5. Database Utilities
Helper functions for common operations:

```python
async def create_health_log(session, model_class, user_id='mcnewcp', **kwargs):
    """Create a new health log record with proper validation."""
    
async def get_recent_logs(session, model_class, user_id='mcnewcp', limit=10):
    """Get recent logs for a user, newest first."""

# Convenience functions for each health log type
async def log_heart_data(session, systolic_mmhg, diastolic_mmhg, rate_bpm, **kwargs):
async def log_body_data(session, weight_lb, smm_lb, pbf, ecw_tcw, **kwargs):
async def log_nutrition_data(session, short_description, protein_g, sodium_mg, potassium_mg, long_description, **kwargs):
async def log_caffeine_data(session, item_description, caffeine_mg, **kwargs):
async def log_alcohol_data(session, item_description, alcohol_oz, **kwargs):
async def log_sauna_data(session, duration_min, **kwargs):
```

## Documentation & References

### SQLAlchemy 2.0 Async
- **Official Guide**: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
- **Migration from 1.x**: https://docs.sqlalchemy.org/en/20/changelog/migration_20.html
- **Async Session Patterns**: Focus on `async_sessionmaker` and context managers

### PostgreSQL Docker
- **Official Image**: https://hub.docker.com/_/postgres
- **Environment Variables**: POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD
- **Initialization Scripts**: Place in `/docker-entrypoint-initdb.d/`

### Alembic with Async
- **Async Environment**: https://alembic.sqlalchemy.org/en/latest/cookbook.html#using-asyncio-with-alembic
- **Auto-generation**: Focus on `alembic revision --autogenerate`

## Key Deliverables

1. **PostgreSQL Container**: Fully configured database service in docker-compose
2. **SQLAlchemy Models**: Six core health log models (heart_log, body_log, nutrition_log, caffeine_log, alcohol_log, sauna_log)
3. **Migration System**: Alembic configuration for schema versioning
4. **Connection Management**: Async database utilities and session management
5. **Database Utilities**: Helper functions for each health log type
6. **Schema Validation**: Database constraints and indexes for data integrity

## Environment Variables Required
Add to `.env.example`:
```bash
# Database Configuration
POSTGRES_URL=postgresql+asyncpg://phda_user:phda_pass@localhost:5432/phda_db
POSTGRES_USER=phda_user
POSTGRES_PASSWORD=phda_pass
POSTGRES_DB=phda_db
```

## Acceptance Criteria

- [ ] PostgreSQL container starts successfully with docker-compose
- [ ] All SQLAlchemy models can be imported without errors
- [ ] `alembic upgrade head` creates all tables successfully
- [ ] Database connection utilities work with async operations
- [ ] All health log models support CRUD operations
- [ ] User isolation works correctly with `user_id` field
- [ ] Database constraints prevent invalid data entry
- [ ] Migration system can handle schema changes
- [ ] Health log utility functions work correctly

## Dependencies
- **Requires**: Feature 1 (Project Structure Setup)
- **Blocks**: Features 5-8 (Agent tools that write to database)

## Estimated Effort
- **Complexity**: Medium
- **Time**: 4-6 hours
- **Risk**: Medium (database setup complexity)

## Notes
- All models follow the database contract specified in CLAUDE.md
- User isolation is built-in but defaults to 'mcnewcp' for Phase 1
- Migration system is set up for future schema evolution
- Async-first design supports high concurrency
- Database constraints ensure data quality and prevent common errors
- Use proper indexes on frequently queried fields (user_id, event_date, type fields)