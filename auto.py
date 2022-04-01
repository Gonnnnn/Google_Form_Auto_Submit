# -*- coding: utf-8 -*- 

import requests
import time
import random

url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeM3Fa2sJH6sedDOQUlwUDDvZgd3M4Nhkkd9y5j9BrkBZA-4w/formResponse'

request_num = 30

def get_answers():
    q1 = ['20세 미만', '20~24세', '25~29세', '30~34세', '35~40세']
    w1 = [1, 5, 4, 1, 1]
    q2 = ['전혀 가지 않는다', '주 1~2회', '주 3~4회', '주 5회 이상']
    w2 = [1, 3, 2, 1]
    q3 = ['마이크 커버가 씌워져있는게 너무 너무 싫다']
    w3 = [1]
    q4 = ['네', '아니오']
    w4 = [8, 1]
    q5 = ['1', '2', '3', '4']
    w5 = [1, 1, 1, 1]
    q61 = ['네', '아니오']
    w61 = [8, 1]
    q62 = ['더러워서']
    w62 = [1]
    questions = [q1, q2, q3, q4, q5, q61, q62]
    weights = [w1, w2, w3, w4, w5, w61, w62]

    answers = []
    for i, q in enumerate(questions):
        if i == 4:
            for j in q:
                answers.append(j)
            continue
        idx = random.choices(range(0, len(q)), weights=weights[i])
        print(idx)
        answers.append(q[idx[0]])

    return answers

for _ in range(request_num):
    answers = get_answers()
    # data = {
    #     'entry.1087171146' : '20~24세',
    #     'entry.1489714317' : '주 3~4회',
    #     'entry.492499245' : '침 냄새가 역하다, 불쾌하다',
    #     'entry.1114282596' : '네',

    #     'entry.465569434' : '1',
    #     'entry.1956967638' : '2',
    #     'entry.1668166955' : '3',
    #     'entry.1751288806' : '4',

    #     'entry.717613266' : '네',
    #     'entry.203425343' : '더러우니까. 이게 맘이 편하다',
    # }

    data = {
    'entry.1087171146' : answers[0],
    'entry.1489714317' : answers[1],
    'entry.492499245' : answers[2],
    'entry.1114282596' : answers[3],

    'entry.465569434' : answers[4],
    'entry.1956967638' : answers[5],
    'entry.1668166955' : answers[6],
    'entry.1751288806' : answers[7],

    'entry.717613266' : answers[8],
    'entry.203425343' : answers[9],
    }
    print(data)

    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

    res = requests.post(url, headers=headers, data=data)
    print(res)
    time.sleep(10)