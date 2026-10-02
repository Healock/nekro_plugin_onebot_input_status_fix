from nekro_agent.api.plugin import NekroPlugin

plugin = NekroPlugin(
    name="OneBot 私聊输入状态修复",
    module_name="nekro_plugin_onebot_input_status_fix",
    description="拦截并修复 OneBot V11 私聊 input_status 通知的频道映射。",
    version="0.1.1",
    author="Healock",
    url="https://github.com/Healock/nekro_plugin_onebot_input_status_fix",
    support_adapter=["onebot_v11"],
)

from . import lifecycle, matcher  # noqa: E402,F401

__all__ = ["plugin"]
