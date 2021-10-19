import pytest
import requests


def test_president_api_call():

    president_list = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe',
                      'Adams', 'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk',
                      'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson',
                      'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison',
                      'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding',
                      'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy',
                      'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton',
                      'Bush', 'Obama', 'Trump', 'Biden']

    url = 'http://api.duckduckgo.com/?q="presidents of the united states"&format=json'
    response = requests.get(url)
    response_json = response.json()
    related_topics = response_json.get('RelatedTopics')

    for item in related_topics:
        text_val = item.get('Text')
        text_list = text_val.split()
        for president in president_list:
            for word in text_list:
                if president == word:
                    president_list.remove(president)
                    break

    assert len(president_list) is 0

