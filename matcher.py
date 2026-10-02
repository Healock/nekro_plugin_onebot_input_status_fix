from __future__ import annotations

from collections import OrderedDict

from nonebot import on_notice
from nonebot.adapters.onebot.v11 import NoticeEvent
from nonebot.rule import Rule

from . import plugin
from .event_filter import event_values, is_onebot_private_input_status, private_chat_key


def _is_onebot_private_input_status(event: NoticeEvent) -> bool:
    return is_onebot_private_input_status(event, NoticeEvent)


input_status_matcher = on_notice(
    rule=Rule(_is_onebot_private_input_status),
    priority=99998,
    block=True,
)
_warned_chat_keys: OrderedDict[str, None] = OrderedDict()
_MAX_WARNED_CHAT_KEYS = 256


def _warn_once(chat_key: str, detail: str) -> None:
    if chat_key in _warned_chat_keys:
        return
    _warned_chat_keys[chat_key] = None
    if len(_warned_chat_keys) > _MAX_WARNED_CHAT_KEYS:
        _warned_chat_keys.popitem(last=False)
    plugin.logger.warning(f"[OneBotInputStatusFix] {detail}: chat={chat_key}")


@input_status_matcher.handle()
async def handle_private_input_status(event: NoticeEvent) -> None:
    values = event_values(event)
    chat_key = private_chat_key(values["user_id"])

    from nekro_agent.models.db_chat_channel import DBChatChannel

    try:
        channel = await DBChatChannel.get_or_none(chat_key=chat_key)
    except Exception as exc:
        _warn_once(chat_key, f"查询私聊频道失败，错误类型={type(exc).__name__}")
        return

    if channel is None:
        _warn_once(chat_key, "私聊输入状态对应频道尚不存在")
        return

    _warned_chat_keys.pop(chat_key, None)
    plugin.logger.debug(f"[OneBotInputStatusFix] 已消费私聊输入状态通知: chat={chat_key}")
