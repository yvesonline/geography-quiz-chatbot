#!/usr/bin/env python3
# encoding: utf-8

import boto3
import copy
import json
import logging
import random
from urllib.parse import parse_qs

import data

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

BODY_QUESTION = {
    'actions': [
        {
            'remember': {}
        },
        {
            'collect': {
                'name': 'questions',
                'questions': [
                    {
                        'question': '',
                        'name': '',
                        'validate': {
                            'on_failure': {
                                'messages': [
                                    {
                                        'say': 'Please answer by typing A, B, C or D.'
                                    }
                                ]
                            },
                            'allowed_values': {
                                'list': ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
                            },
                            'max_attempts': {
                                'redirect': 'task://collect_fallback',
                                'num_attempts': 3
                            }
                        }
                    }
                ],
                'on_complete': {
                    'redirect': ''
                }
            }
        }
    ]
}

BODY_ANSWER = {
    'actions': [
        {
            'say': ''
        },
        {
            'remember': {}
        },
        {
            'listen': True
        }
    ]
}


def capital(event, context):
    logger.debug(f'event: {event}')
    logger.debug(f'context: {context}')

    body = copy.deepcopy(BODY_QUESTION)

    choices = list(data.COUNTRY_TO_CAPITAL.keys())

    answer_keys = []

    random_answer_key = random.choice(choices)

    while len(answer_keys) < 4 and random_answer_key not in answer_keys:
        answer_keys.append(random_answer_key)
        random_answer_key = random.choice(choices)

    answers = {c: {
        'country': answer_keys[i],
        'capital': data.COUNTRY_TO_CAPITAL[answer_keys[i]],
    } for c, i in zip(['A', 'B', 'C', 'D'], range(4))}

    correct_choice = random.choice([(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')])

    body['actions'][0]['remember'] = {
        'correct_answer_idx': correct_choice[0],
        'correct_answer_key': correct_choice[1],
        'correct_answer_country': answers[correct_choice[1]]['country'],
        'correct_answer_capital': answers[correct_choice[1]]['capital'],
    }
    question = f"What's the capital of {answers[correct_choice[1]]['country']}?\n"
    question += "\n".join([f"{option}) {answer['capital']}" for option, answer in answers.items()])
    body['actions'][1]['collect']['questions'][0]['question'] = question
    body['actions'][1]['collect']['questions'][0]['name'] = 'capital'
    body['actions'][1]['collect']['on_complete']['redirect'] = \
        'https://87cwtct4i0.execute-api.eu-west-2.amazonaws.com/dev/gqb/capital-check'

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response


def capital_check(event, context):
    logger.debug(f'event: {event}')
    logger.debug(f'context: {context}')

    body = copy.deepcopy(BODY_ANSWER)

    event_body = parse_qs(event['body'])
    memory = json.loads(event_body['Memory'][0])

    # score_total
    # score_correct
    scores = {}
    for score_item in ['score_total', 'score_correct']:
        if score_item in memory:
            scores[score_item] = int(memory[score_item])
        else:
            scores[score_item] = 0

    scores['score_total'] += 1

    if memory['correct_answer_key'].lower() == \
       memory['twilio']['collected_data']['questions']['answers']['capital']['answer'].lower():
        say = "Yes you're right, "
        scores['score_correct'] += 1
    else:
        say = "No that's wrong, "
    say += f"{memory['correct_answer_capital']} is the capital of {memory['correct_answer_country']}.\n"
    say += f"You've got {scores['score_correct']} out of {scores['score_total']} right so far!"

    body['actions'][0]['say'] = say

    body['actions'][1]['remember'] = {
        'score_total': scores['score_total'],
        'score_correct': scores['score_correct'],
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response


def country(event, context):
    logger.debug(f'event: {event}')
    logger.debug(f'context: {context}')

    body = copy.deepcopy(BODY_QUESTION)

    s3_client = boto3.client('s3')
    bucket = 'geography-quiz-bot-images'
    base_url = f'https://{bucket}.s3.eu-west-2.amazonaws.com/'

    response = s3_client.list_objects(Bucket=bucket, MaxKeys=300)

    choices = [country['Key'] for country in response['Contents']]

    answer_keys = []

    random_answer_key = random.choice(choices)

    while len(answer_keys) < 4 and random_answer_key not in answer_keys:
        answer_keys.append(random_answer_key)
        random_answer_key = random.choice(choices)

    answers = {c: {
        'country_name': answer_keys[i].split('-')[0].replace('_', ' '),
        'country_iso': answer_keys[i].split('-')[1][:3],
        'country_filename': answer_keys[i],
    } for c, i in zip(['A', 'B', 'C', 'D'], range(4))}
    logger.debug(f'answers: {answers}')

    correct_choice = random.choice([(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')])

    body['actions'][0]['remember'] = {
        'correct_answer_idx': correct_choice[0],
        'correct_answer_key': correct_choice[1],
        'correct_answer_country_name': answers[correct_choice[1]]['country_name'],
        'correct_answer_country_iso': answers[correct_choice[1]]['country_iso'],
        'correct_answer_country_filename': answers[correct_choice[1]]['country_filename'],
    }
    question = 'Which country are we looking at here?\n'
    question += "\n".join([f"{option}) {answer['country_name']}" for option, answer in answers.items()])
    body['actions'][1]['collect']['questions'][0]['question'] = question
    body['actions'][1]['collect']['questions'][0]['name'] = 'country'
    body['actions'][1]['collect']['on_complete']['redirect'] = \
        'https://87cwtct4i0.execute-api.eu-west-2.amazonaws.com/dev/gqb/country-check'

    logger.debug(f'body: {body}')

    image_url = f"{base_url}{answers[correct_choice[1]]['country_filename']}"
    image_action = {
        'show': {
            'body': 'Mysterious country',
            'images': [{
                'label': 'Mysterious country',
                'url': image_url
            }]
        }
    }
    body['actions'].insert(0, image_action)

    logger.debug(f'image_action: {image_action}')
    logger.debug(f'body: {body}')

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response


def country_check(event, context):
    logger.debug(f'event: {event}')
    logger.debug(f'context: {context}')

    body = copy.deepcopy(BODY_ANSWER)

    event_body = parse_qs(event['body'])
    memory = json.loads(event_body['Memory'][0])

    # score_total
    # score_correct
    scores = {}
    for score_item in ['score_total', 'score_correct']:
        if score_item in memory:
            scores[score_item] = int(memory[score_item])
        else:
            scores[score_item] = 0

    scores['score_total'] += 1

    if memory['correct_answer_key'].lower() == \
       memory['twilio']['collected_data']['questions']['answers']['country']['answer'].lower():
        say = "Yes you're right, "
        scores['score_correct'] += 1
    else:
        say = "No that's wrong, "
    say += f"this is {memory['correct_answer_country_name']} ({memory['correct_answer_country_iso']}).\n"
    say += f"You've got {scores['score_correct']} out of {scores['score_total']} right so far!"

    body['actions'][0]['say'] = say

    body['actions'][1]['remember'] = {
        'score_total': scores['score_total'],
        'score_correct': scores['score_correct'],
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response
