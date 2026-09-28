from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def event_values(event: Any) -> Mapping[str, Any]:
    if isinstance(event, Mapping):
        return event
    if hasattr(event, "dict"):
        values = event.dict()
        return values if isinstance(values, Mapping) else {}
    try:
        return dict(event)
    except (TypeError, ValueError):
        return {}


def is_private_input_status(event: Any) -> bool:
    values = event_values(event)
    return (
        values.get("notice_type") == "notify"
        and values.get("sub_type") == "input_status"
        and str(values.get("group_id", "")) == "0"
        and bool(values.get("user_id"))
    )


def private_chat_key(user_id: Any) -> str:
    return f"onebot_v11-private_{user_id}"
