import time
from hack_aggregator import hack_api
from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .models import Content

def prepareContent(content):
    savedContent = {}
    savedContent['id'] = content['unique_id']
    savedContent['created_at'] = content['creation_info']['created_at']
    savedContent['author'] = content['author']['id']
    savedContent['main_text'] = content['context']['main_text']
    savedContent['origin_url'] = content['origin_details']['origin_url']
    savedContent['media'] = content['media']['urls']
    savedContent['likes'] = content['stats']['digg_counts']['likes']['count']
    savedContent['views'] = content['stats']['digg_counts']['views']['count']
    savedContent['comments'] = content['stats']['digg_counts']['comments']['count']
    return savedContent


@shared_task
def updateDb():
    page = 1
    while page == 1:
        content_list_response = hack_api.get_content_list(page)
        if content_list_response.status_code == 200:
            json_res = content_list_response.json()
            for item in json_res['data']:
                preppedContent  = prepareContent(item)
                contentInstance = Content(**preppedContent).save()
            page = json_res['next']
        else:
            time.sleep(3)
            continue

# Create schedule
schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,  # You can change the interval here
    period=IntervalSchedule.SECONDS,
)

# Schedule the task
PeriodicTask.objects.get_or_create(
    interval=schedule,
    name='Update DB',  # Name of the task
    task='hack_aggregator.tasks.updateDb',  # Task name, which is the name you used in the @shared_task decorator
)