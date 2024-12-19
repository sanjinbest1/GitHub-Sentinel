# GitHub Sentinel

GitHub Sentinel is an open-source AI-powered tool designed for developers and project managers to automatically collect and summarize the latest updates from subscribed GitHub repositories on a regular basis (daily/weekly). The primary features of GitHub Sentinel include repository subscription management, update fetching, notification system, and report generation. By keeping track of the latest repository changes and pushing notifications to users, GitHub Sentinel significantly enhances team collaboration and project management, allowing users to efficiently monitor project progress, respond quickly to changes, and ensure that the project remains up to date.

[中文版 README](docs/README_CN.md)

## Features

- **Repository Subscription Management**: Subscribe to GitHub repositories to automatically track their updates.
- **Update Fetching**: Automatically fetch updates from subscribed repositories, including pull requests, issues, releases, and commits.
- **Notification System**: Receive notifications about the latest updates from repositories in your subscription list.
- **Report Generation**: Generate detailed reports on the progress and updates of the repositories for team review.

## Getting Started

### Prerequisites

To run GitHub Sentinel, you need to have the following tools installed:

- Python 3.7 or higher
- GitHub API Token (can be generated from GitHub's Developer Settings)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/GitHub-Sentinel.git
   ```

2. Install required dependencies:

   ```bash
   cd GitHub-Sentinel
   pip install -r requirements.txt
   ```

3. Set up your GitHub API credentials in `config/settings.py`.

4. Run the program:

   ```bash
   python main.py
   ```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- GitHub API
- Python
