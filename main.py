import argparse
from service.report_service import fetch_and_generate_reports, generate_reports
from service.subscription_service import subscription_management
from scheduler.scheduler import schedule_reports

def display_help():
    """显示帮助信息"""
    print("""
    可用的命令：
    1. fetch - 获取并生成报告
    2. report - 生成报告
    3. subscription - 订阅管理
    4. schedule - 设置定时任务调度
    0. exit - 退出程序
    """)

def main():
    print("Welcome to GitHub Sentinel CLI!")
    print("Type 'help' to see available commands.")

    while True:
        # 获取用户输入的命令
        command = input("\n请输入命令: ").strip().lower()

        # 根据命令执行相应的操作
        if command == "fetch":
            fetch_and_generate_reports()
        elif command == "report":
            generate_reports()
        elif command == "subscription":
            subscription_management()
        elif command == "schedule":
            schedule_reports()
        elif command == "help":
            display_help()
        elif command == "exit":
            print("Exiting GitHub Sentinel CLI. Goodbye!")
            break  # 退出程序
        else:
            print("无效的命令，请输入 'help' 查看可用命令。")

if __name__ == "__main__":
    main()
