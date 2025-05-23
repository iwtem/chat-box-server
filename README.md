# Chat Box Server

一个简单的聊天盒子服务器项目。

## 项目简介

这是一个基于 Python 的聊天服务器项目，用于提供聊天盒子功能。

## 环境要求

- Python >= 3.13

## 安装

1. 克隆项目到本地：

```bash
git clone <repository-url>
cd chat-box-server
```

2. 安装项目依赖：

```bash
pip install -e .
```

## 使用方法

运行服务器：

```bash
python main.py
```

## 项目结构

```plaintext
chat-box-server/
├── README.md           # 项目说明文档
├── main.py            # 主程序入口
├── pyproject.toml     # 项目配置文件
└── .python-version    # Python 版本指定
```

## 开发计划

- [ ] 实现基础聊天服务器功能
- [ ] 添加用户认证系统
- [ ] 支持多房间聊天
- [ ] 添加消息持久化
- [ ] 实现 WebSocket 连接
