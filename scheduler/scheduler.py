import threading
import time
from core.update_fetcher import fetch_and_generate_reports

def scheduler_job():
    """Background scheduler job to fetch updates."""
    while True:
        print("[Scheduler] Fetching updates...")
        fetch_and_generate_reports()
        print("[Scheduler] Sleeping for 24 hours...")
        time.sleep(86400)  # Run daily

def start_scheduler():
    """Start the scheduler in a separate thread."""
    scheduler_thread = threading.Thread(target=scheduler_job, daemon=True)
    scheduler_thread.start()
