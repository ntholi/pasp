from django import template
from datetime import datetime, timedelta, timezone

register = template.Library()


@register.filter(name="now_or_after")
def now_or_after(start_time: datetime):
    """Return True if start_time is in the past or now, False otherwise."""
    now = datetime.now(timezone.utc)
    print(f"{start_time.tzinfo=}")
    return start_time <= now
