from sqlalchemy import Column, Integer, String, DateTime, Float
from .base import Base

class HeartLog(Base):
    __tablename__ = 'heart_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    systolic_mmhg = Column(Integer, nullable=False)
    diastolic_mmhg = Column(Integer, nullable=False)
    rate_bpm = Column(Integer, nullable=False)

class BodyLog(Base):
    __tablename__ = 'body_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    weight_lb = Column(Float, nullable=False)
    smm_lb = Column(Float, nullable=False)
    pbf = Column(Float, nullable=False)
    ecw_tcw = Column(Float, nullable=False)

class NutritionLog(Base):
    __tablename__ = 'nutrition_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    short_description = Column(String(255), nullable=False)
    protein_g = Column(Float, nullable=False)
    sodium_mg = Column(Float, nullable=False)
    potassium_mg = Column(Float, nullable=False)
    long_description = Column(String, nullable=False)

class CaffeineLog(Base):
    __tablename__ = 'caffeine_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    item_description = Column(String(255), nullable=False)
    caffeine_mg = Column(Float, nullable=False)

class AlcoholLog(Base):
    __tablename__ = 'alcohol_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    item_description = Column(String(255), nullable=False)
    alcohol_oz = Column(Float, nullable=False)

class SaunaLog(Base):
    __tablename__ = 'sauna_log'
    
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), nullable=False)
    duration_min = Column(Integer, nullable=False)