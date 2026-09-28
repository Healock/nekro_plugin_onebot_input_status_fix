from __future__ import annotations

from . import plugin
from .matcher import input_status_matcher


@plugin.mount_cleanup_method()
async def cleanup() -> None:
    destroy = getattr(input_status_matcher, "destroy", None)
    if not callable(destroy):
        return
    try:
        destroy()
    except (KeyError, ValueError):
        return
