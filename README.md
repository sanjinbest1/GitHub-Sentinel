# GitHub Sentinel

GitHub Sentinel 是一款开源的 AI 工具，专为开发者和项目管理人员设计，能够定期（每日/每周）自动获取并汇总订阅的 GitHub 仓库的最新动态。GitHub Sentinel 的主要功能包括仓库订阅管理、更新获取、通知系统和报告生成。通过实时获取和推送仓库的最新更新，GitHub Sentinel 大大提高了团队协作效率和项目管理的便捷性，帮助用户高效跟踪项目进展，快速响应变更，确保项目始终保持最新状态。

[English README](docs/README_EN.md)

## 功能

- **仓库订阅管理**: 订阅 GitHub 仓库，自动跟踪其更新。
- **更新获取**: 自动获取订阅仓库的最新动态，包括拉取请求、问题、发布和提交等。
- **通知系统**: 获取关于订阅仓库最新更新的通知。
- **报告生成**: 生成详细的仓库进度和更新报告，供团队评审。

## 快速开始

### 前提条件

要运行 GitHub Sentinel，您需要安装以下工具：

- Python 3.7 或更高版本
- GitHub API 令牌（可以从 GitHub 开发者设置中生成）

### 安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/yourusername/GitHub-Sentinel.git
   ```

2. 安装所需的依赖：

   ```bash
   cd GitHub-Sentinel
   pip install -r requirements.txt
   ```

3. 在 `config/settings.py` 中配置您的 GitHub API 凭证。

4. 运行程序：

   ```bash
   python main.py
   ```

## 项目结构

```
GitHub-Sentinel/
├── config/
│   ├── settings.py          # 配置文件（如 GitHub API 凭证、通知设置等）
├── core/
│   ├── __init__.py
│   ├── github_api.py       # 与 GitHub API 交互
│   ├── subscription.py     # 管理仓库订阅
│   ├── update_fetcher.py   # 获取仓库更新
│   ├── report_generator.py # 生成更新报告
│   ├── notification.py     # 通知系统
├── data/
│   ├── __init__.py
│   ├── data_store.py       # 存储和检索仓库数据
├── scheduler/
│   ├── __init__.py
│   ├── scheduler.py        # 定时任务调度（每日/每周更新）
├── tests/
│   ├── test_github_api.py  # GitHub API 交互测试
│   ├── test_subscription.py # 订阅管理单元测试
│   ├── test_update_fetcher.py # 更新获取单元测试
│   ├── test_report_generator.py # 报告生成单元测试
│   ├── test_notification.py # 通知系统单元测试
└── main.py                  # 启动程序
```

## 许可证

本项目采用 MIT 许可证 - 详细信息请参见 [LICENSE](LICENSE) 文件。

## 致谢

- GitHub API
- Python
