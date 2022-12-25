from celery import shared_task


@shared_task(bind=True)
def loop_task(self):
    # operation
    for i in range(10):
        print(i)
    return "Done"