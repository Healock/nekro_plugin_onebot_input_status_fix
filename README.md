# NekroAgent OneBot 私聊输入状态修复

> 处理 OneBot V11 私聊输入状态通知的频道映射问题，不改变消息和 Agent 行为。

## 快速开始

将整个 `nekro_plugin_onebot_input_status_fix` 目录放入 NekroAgent 数据目录的插件工作区：

```text
DATA_DIR/plugins/workdir/nekro_plugin_onebot_input_status_fix/
```

插件适配器限定为 OneBot V11。

## 功能范围

- 只拦截 `group_id=0` 的 `notify/input_status` 通知。
- 按 `onebot_v11-private_<user_id>` 检查对应私聊频道。
- 频道不存在或查询失败时，对同一频道最多记录一次 warning；频道恢复后重新启用告警。
- 仅消费通知并记录日志，不注入提示词、不触发 Agent，也不修改普通私聊消息流程。
- 群聊输入状态和其他通知继续由 NekroAgent 原有处理链路处理。

## 插件结构

```text
nekro_plugin_onebot_input_status_fix/
├── __init__.py       # 插件定义与模块加载
├── event_filter.py   # 输入状态事件筛选和频道键构造
├── matcher.py        # OneBot 通知 matcher
└── lifecycle.py      # matcher 清理
```

## 开发

```powershell
python -m pytest -q tests
python -m py_compile *.py
```

本地静态测试不能替代真实 NekroAgent 和 OneBot V11 环境验证。

## 相关资源

- [NekroAgent 官方文档](https://doc.nekro.ai/)
- [插件开发快速上手](https://doc.nekro.ai/docs/04_plugin_dev/01_quick_start.html)
- [Nekro 插件模板](https://github.com/KroMiose/nekro-plugin-template)
