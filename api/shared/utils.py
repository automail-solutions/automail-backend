import time
from typing import Any, Dict


def get_current_timestamp() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def create_metadata(processing_time: float) -> Dict[str, Any]:
    return {
        "processing_time": processing_time,
        "timestamp": get_current_timestamp()
    }