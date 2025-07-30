from apscheduler.schedulers.background import BackgroundScheduler

def scheduled_task():
    print("Task executed!")

scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_task, 'interval', seconds=30)
scheduler.start()