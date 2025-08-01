from datetime import datetime
from typing import Dict, Any
from langchain_core.tools import tool
from shared.models.health_logs import HeartLog, BodyLog, SaunaLog
from shared.utils.database import get_session

@tool
def log_heart_data(
    datetime_value: datetime,
    systolic_mmhg: int,
    diastolic_mmhg: int,
    rate_bpm: int
) -> Dict[str, Any]:
    """
    Log heart rate and blood pressure data.
    
    Args:
        datetime_value: When the measurement was taken
        systolic_mmhg: Systolic blood pressure in mmHg
        diastolic_mmhg: Diastolic blood pressure in mmHg
        rate_bpm: Heart rate in beats per minute
        
    Returns:
        Dictionary with success status and logged data
    """
    try:
        with get_session() as session:
            heart_log = HeartLog(
                datetime=datetime_value,
                systolic_mmhg=systolic_mmhg,
                diastolic_mmhg=diastolic_mmhg,
                rate_bpm=rate_bpm
            )
            session.add(heart_log)
            session.commit()
            
        return {
            "success": True,
            "logged": "heart data",
            "datetime": datetime_value.isoformat(),
            "systolic": systolic_mmhg,
            "diastolic": diastolic_mmhg,
            "heart_rate": rate_bpm
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

@tool
def log_body_data(
    datetime_value: datetime,
    weight_lb: float,
    smm_lb: float,
    pbf: float,
    ecw_tcw: float
) -> Dict[str, Any]:
    """
    Log body composition data.
    
    Args:
        datetime_value: When the measurement was taken
        weight_lb: Body weight in pounds
        smm_lb: Skeletal muscle mass in pounds
        pbf: Percent body fat
        ecw_tcw: Extracellular water to total cell water ratio
        
    Returns:
        Dictionary with success status and logged data
    """
    try:
        with get_session() as session:
            body_log = BodyLog(
                datetime=datetime_value,
                weight_lb=weight_lb,
                smm_lb=smm_lb,
                pbf=pbf,
                ecw_tcw=ecw_tcw
            )
            session.add(body_log)
            session.commit()
            
        return {
            "success": True,
            "logged": "body composition",
            "datetime": datetime_value.isoformat(),
            "weight": weight_lb,
            "muscle_mass": smm_lb,
            "body_fat": pbf,
            "water_ratio": ecw_tcw
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

@tool
def log_sauna_data(
    datetime_value: datetime,
    duration_min: int
) -> Dict[str, Any]:
    """
    Log sauna session data.
    
    Args:
        datetime_value: When the sauna session occurred
        duration_min: Duration of the session in minutes
        
    Returns:
        Dictionary with success status and logged data
    """
    try:
        with get_session() as session:
            sauna_log = SaunaLog(
                datetime=datetime_value,
                duration_min=duration_min
            )
            session.add(sauna_log)
            session.commit()
            
        return {
            "success": True,
            "logged": "sauna session",
            "datetime": datetime_value.isoformat(),
            "duration": duration_min
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }