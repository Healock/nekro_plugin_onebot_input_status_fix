from __future__ import annotations

from nekro_plugin_onebot_input_status_fix.event_filter import is_private_input_status, private_chat_key


def test_matches_only_private_input_status_notice() -> None:
    event = {"notice_type": "notify", "sub_type": "input_status", "group_id": 0, "user_id": 123}

    assert is_private_input_status(event)
    assert private_chat_key(event["user_id"]) == "onebot_v11-private_123"


def test_does_not_match_group_input_status() -> None:
    event = {"notice_type": "notify", "sub_type": "input_status", "group_id": 456, "user_id": 123}

    assert not is_private_input_status(event)


def test_does_not_match_other_notice_types() -> None:
    assert not is_private_input_status(
        {"notice_type": "notify", "sub_type": "poke", "group_id": 0, "user_id": 123},
    )
    assert not is_private_input_status(
        {"notice_type": "group_increase", "sub_type": "input_status", "group_id": 456, "user_id": 123},
    )
