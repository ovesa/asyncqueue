from pydantic import BaseModel, field_validator
from typing import Optional, Any
from enum import Enum
import uuid
from datetime import datetime

class JobStatus(str, Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"
    cancelled = "cancelled"

class JobCreate(BaseModel):
    task_name: str
    payload: dict[str, Any] = {}
    webhook_url: Optional[str] = None
    priority: int = 0

    @field_validator("task_name")
    @classmethod
    def task_name_must_be_valid(cls, v):
        allowed = ["run_simulation", "process_dataset", "generate_report", "send_webhook_test", "cleanup_old_jobs"]
        if v not in allowed:
            raise ValueError(f"task_name must be one of {allowed}")
        return v
class JobResponse(BaseModel):
    id: str
    status: JobStatus
    task_name: str
    payload: dict[str, Any]
    result: Optional[Any] = None
    error: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class JobListResponse(BaseModel):
    jobs: list[JobResponse]
    total: int