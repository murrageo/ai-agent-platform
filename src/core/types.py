from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

# ---------------------------
# Namespaces
# ---------------------------

class MetaNamespace(BaseModel):
    run_id: Optional[str] = None
    workflow: Optional[str] = None
    created_at: Optional[datetime] = None
    prompt_versions: Dict[str, str] = Field(default_factory=dict)


class ContentNamespace(BaseModel):
    topic: Optional[str] = None
    research: Optional[Dict[str, Any]] = None
    draft: Optional[str] = None
    final: Optional[str] = None
    ideas: List[str] = Field(default_factory=list)


class DevNamespace(BaseModel):
    requirements: Optional[Dict[str, Any]] = None
    architecture_plan: Optional[Dict[str, Any]] = None
    code_patch: Optional[str] = None
    tests: Optional[str] = None


class MetricsNamespace(BaseModel):
    content_scores: Dict[str, float] = Field(default_factory=dict)
    dev_scores: Dict[str, float] = Field(default_factory=dict)
    cost_log: List[Dict[str, Any]] = Field(default_factory=list)

# ---------------------------
# Global State Contract
# ---------------------------

class State(BaseModel):
    meta: MetaNamespace = Field(default_factory=MetaNamespace)
    content: ContentNamespace = Field(default_factory=ContentNamespace)
    dev: DevNamespace = Field(default_factory=DevNamespace)
    metrics: MetricsNamespace = Field(default_factory=MetricsNamespace)

# ---------------------------
# Task Definition
# ---------------------------

class Task(BaseModel):
    task_id: Optional[str] = None
    task_type: Optional[str] = None
    payload: Dict[str, Any] = Field(default_factory=dict)

# ---------------------------
# Artifact Definition
# ---------------------------

class Artifact(BaseModel):
    artifact_id: Optional[str] = None
    artifact_type: Optional[str] = None
    content: Any = None
    created_at: Optional[datetime] = None

# ---------------------------
# Event Definition
# ---------------------------

class Event(BaseModel):
    event_type: str
    source_agent: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

