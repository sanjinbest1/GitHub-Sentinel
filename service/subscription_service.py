import argparse
from core.subscription import add_subscription, remove_subscription, list_subscriptions

def subscription_management():
    """处理订阅管理相关的命令"""
    parser = argparse.ArgumentParser(description="Subscription Management")
    parser.add_argument("action", choices=["subscribe", "unsubscribe", "list"], help="Subscription management action")
    parser.add_argument("--repo", type=str, help="Repository to subscribe or unsubscribe")

    args = parser.parse_args()

    if args.action == "subscribe":
        if not args.repo:
            print("Repository name is required to subscribe.")
        else:
            print(add_subscription(args.repo))
    elif args.action == "unsubscribe":
        if not args.repo:
            print("Repository name is required to unsubscribe.")
        else:
            print(remove_subscription(args.repo))
    elif args.action == "list":
        subscriptions = list_subscriptions()
        if subscriptions:
            print("Subscribed repositories:")
            for repo in subscriptions:
                print(f"- {repo}")
        else:
            print("No subscriptions found.")
