
import json
from time import sleep
from bs4 import BeautifulSoup
from kafka import KafkaConsumer, TopicPartition

def parse(markup):
    title = '-'
    submit_by = '-'
    description = '-'
    calories = 0
    ingredients = []
    rec = {}

    try:

        soup = BeautifulSoup(markup, 'lxml')
        # title
        title_section = soup.find_all("h1", {"class": "headline heading-content elementFont__display"})
        # submitter
        submitter_section = soup.select(".author-name")
        # description
        description_section = soup.find_all("p", {"class": "margin-0-auto"})
        # ingredients
        ingredients_section = soup.find_all("span", {"class": "ingredients-item-name elementFont__body"})
        # calories
        calories_section = soup.find_all("div", {"class": "section-body"})

        if title_section:
            title = title_section[0].text

        if submitter_section:
            submit_by = submitter_section[0].text

        if description_section:
            description = description_section[0].text.strip().replace('"', '')

        if ingredients_section:
            for ingredient in ingredients_section:
                ingredient_text = ingredient.text.strip()
                if 'Add all ingredients to list' not in ingredient_text and ingredient_text != '':
                    ingredients.append({'step': ingredient.text.strip()})

        if calories_section:
            calories = calories_section[-1].text.split(';')[0]

        rec = {'title': title, 'submitter': submit_by, 'description': description, 'calories': calories,
               'ingredients': ingredients}

    except Exception as ex:
        print('Exception while parsing')
        print(str(ex))
    finally:
        return json.dumps(rec)


print('Running Consumer..')
parsed_records = []
topic_name = 'raw_recipes'

consumer = KafkaConsumer(
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest'
)
consumer.subscribe([topic_name])
while True:
    records = consumer.poll(timeout_ms=1000)
    for topic_data, consumer_records in records.items():
        print('--------------- TOPIC ---------------')
        print(topic_data)
        for consumer_record in consumer_records:
            print('-------------- MESSAGE --------------')
            print(parse(consumer_record.value.decode('utf-8')))
        print('-------------------------------------')
