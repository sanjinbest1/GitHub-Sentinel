import schedule
import time
from core.update_fetcher import UpdateFetcher
from core.report_generator import ReportGenerator
from core.notification import NotificationSystem

class Scheduler:
    def __init__(self):
        self.update_fetcher = UpdateFetcher()
        self.report_generator = ReportGenerator()
        self.notification_system = NotificationSystem()

    def schedule_daily_update(self):
        schedule.every().day.at("09:00").do(self.run_task)

    def schedule_weekly_update(self):
        schedule.every().monday.at("09:00").do(self.run_task)

    def run_task(self):
        updates = self.update_fetcher.fetch_updates()
        report = self.report_generator.generate_report(updates)
        self.notification_system.send_email("user@example.com", "Daily GitHub Updates", report)
        
    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
