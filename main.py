import argparse
from core.subscription import add_subscription, remove_subscription, list_subscriptions
from core.update_fetcher import fetch_and_generate_reports
from core.github_api import fetch_latest_release
from core.report_generator import generate_report
from scheduler.scheduler import start_scheduler


def subscribe(repo):
    print(add_subscription(repo))


def unsubscribe(repo):
    print(remove_subscription(repo))


def list_repos():
    print("Subscribed repositories:")
    print(list_subscriptions())


def fetch_all():
    print("Fetching updates for all subscriptions...")
    fetch_and_generate_reports()


def fetch_repo(repo):
    try:
        print(f"Fetching latest release for {repo}...")
        release = fetch_latest_release(repo)
        print(f"Latest release: {release.get('tag_name', 'N/A')} - {release.get('name', 'N/A')}")
    except Exception as e:
        print(f"Error fetching updates for {repo}: {e}")


def generate_repo_report(repo):
    try:
        print(f"Generating report for {repo}...")
        release = fetch_latest_release(repo)
        report_path = generate_report(release, repo)
        print(f"Report generated: {report_path}")
    except Exception as e:
        print(f"Error generating report for {repo}: {e}")


def print_help():
    print("""
GitHub Sentinel Interactive Tool (gs)
Commands:
  subscribe <repo>      Subscribe to a repository (e.g., owner/repo)
  unsubscribe <repo>    Unsubscribe from a repository
  list                  List all subscribed repositories
  fetch [repo]          Fetch updates for all or a specific repository
  report <repo>         Generate a report for a specific repository
  exit                  Exit the tool
""")


def main():
    # Start scheduler in the background
    start_scheduler()
    print("[Scheduler] Running in the background...\n")

    print("Welcome to GitHub Sentinel Interactive Tool!")
    print_help()

    while True:
        # Prompt user for input
        user_input = input("\n> ").strip()
        if not user_input:
            continue

        # Split input into command and arguments
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        # Command handling
        if command == "subscribe":
            if len(args) != 1:
                print("Usage: subscribe <repo>")
            else:
                subscribe(args[0])
        elif command == "unsubscribe":
            if len(args) != 1:
                print("Usage: unsubscribe <repo>")
            else:
                unsubscribe(args[0])
        elif command == "list":
            list_repos()
        elif command == "fetch":
            if len(args) == 0:
                fetch_all()
            elif len(args) == 1:
                fetch_repo(args[0])
            else:
                print("Usage: fetch [repo]")
        elif command == "report":
            if len(args) != 1:
                print("Usage: report <repo>")
            else:
                generate_repo_report(args[0])
        elif command in {"exit", "quit"}:
            print("Exiting GitHub Sentinel. Goodbye!")
            break
        else:
            print(f"Unknown command: {command}")
            print_help()


if __name__ == "__main__":
    main()
