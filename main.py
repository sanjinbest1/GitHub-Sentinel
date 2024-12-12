from scheduler.scheduler import Scheduler

def main():
    scheduler = Scheduler()
    scheduler.schedule_daily_update()
    scheduler.run()

if __name__ == "__main__":
    main()
