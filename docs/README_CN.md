# GitHub Sentinel

GitHub Sentinel 是一款开源的 AI 工具，专为开发者和项目管理人员设计，能够定期（每日/每周）自动获取并汇总订阅的 GitHub 仓库的最新动态。GitHub Sentinel 的主要功能包括仓库订阅管理、更新获取、通知系统和报告生成。通过实时获取和推送仓库的最新更新，GitHub Sentinel 大大提高了团队协作效率和项目管理的便捷性，帮助用户高效跟踪项目进展，快速响应变更，确保项目始终保持最新状态。

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

## 许可证

本项目采用 MIT 许可证 - 详细信息请参见 [LICENSE](LICENSE) 文件。

## 致谢

- GitHub API
- Python
