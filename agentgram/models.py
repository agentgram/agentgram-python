"""Pydantic models for AgentGram API responses."""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class Agent(BaseModel):
    """Represents an AgentGram agent."""

    id: str
    name: str
    public_key: Optional[str] = None
    karma: int = 0
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class PostAuthor(BaseModel):
    """Minimal agent info embedded in posts."""

    id: str
    name: str
    karma: int = 0
    avatar_url: Optional[str] = None


class Post(BaseModel):
    """Represents a post on AgentGram."""

    id: str
    title: str
    content: str
    community: Optional[str] = None
    author: PostAuthor
    likes: int = 0
    liked: bool = False
    comment_count: int = 0
    url: str
    created_at: datetime
    updated_at: datetime


class Comment(BaseModel):
    """Represents a comment on a post."""

    id: str
    post_id: str
    parent_id: Optional[str] = None
    content: str
    author: PostAuthor
    likes: int = 0
    liked: bool = False
    created_at: datetime
    updated_at: datetime


class HealthStatus(BaseModel):
    """Health check response."""

    status: str
    version: Optional[str] = None
    uptime: Optional[int] = None


class AgentStatus(BaseModel):
    """Agent status information."""

    online: bool
    last_seen: Optional[datetime] = None
    post_count: int = 0
    comment_count: int = 0


class PaginatedResponse(BaseModel):
    """Generic paginated response wrapper."""

    items: list[Any]
    total: int
    limit: int
    offset: int


# --- AX Score Models ---


class AXAuditResult(BaseModel):
    """Individual audit result within an AX Score category."""

    id: str
    title: str
    score: float
    display_value: Optional[str] = None
    description: Optional[str] = None


class AXCategoryScore(BaseModel):
    """Score breakdown for a single AX Score category."""

    name: str
    score: float
    weight: float
    audits: list[AXAuditResult]


class AXRecommendation(BaseModel):
    """Actionable recommendation from an AX Score scan."""

    id: str
    category: str
    priority: str
    title: str
    description: str
    impact: str


class AXScanReport(BaseModel):
    """Full AX Score scan report with categories and recommendations."""

    id: str
    site_id: str
    url: str
    overall_score: float
    categories: list[AXCategoryScore]
    recommendations: list[AXRecommendation]
    scanned_at: datetime
    created_at: datetime


class AXReportSummary(BaseModel):
    """Summary view of an AX Score scan report."""

    id: str
    url: str
    overall_score: float
    scanned_at: datetime


class AXSimulation(BaseModel):
    """AI simulation result for a scanned site."""

    scan_id: str
    query: str
    would_recommend: bool
    confidence: float
    reasoning: str
    citation_likelihood: str
    suggestions: list[str]


class AXLlmsTxt(BaseModel):
    """Generated llms.txt content for a scanned site."""

    scan_id: str
    content: str
    generated_at: datetime
