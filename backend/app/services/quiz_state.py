import random

MASTER_POOL = [
    {
        "topic": "addition",
        "question": "5 + 5 = ?",
        "answer": "10"
    },
    {
        "topic": "subtraction",
        "question": "8 - 3 = ?",
        "answer": "5"
    }
]

ACTIVE_POOL = []

TOPIC_MASTERY = {}

GENERATED_QUESTIONS = set()


def reset_quiz():

    global ACTIVE_POOL
    global TOPIC_MASTERY
    global GENERATED_QUESTIONS

    ACTIVE_POOL = MASTER_POOL.copy()

    TOPIC_MASTERY = {
        item["topic"]: 0
        for item in MASTER_POOL
    }

    GENERATED_QUESTIONS.clear()

    for item in MASTER_POOL:

        GENERATED_QUESTIONS.add(
            item["question"].strip()
        )

    print("QUIZ RESET")
    print(ACTIVE_POOL)


def get_random_question():

    if len(ACTIVE_POOL) == 0:
        return None

    return random.choice(ACTIVE_POOL)


def increase_mastery(topic):

    if topic not in TOPIC_MASTERY:
        TOPIC_MASTERY[topic] = 0

    TOPIC_MASTERY[topic] += 1

    print(f"{topic} mastery increased:")
    print(TOPIC_MASTERY[topic])


def decrease_mastery(topic):

    if topic not in TOPIC_MASTERY:
        TOPIC_MASTERY[topic] = 0

    TOPIC_MASTERY[topic] = max(
        0,
        TOPIC_MASTERY[topic] - 1
    )

    print(f"{topic} mastery decreased:")
    print(TOPIC_MASTERY[topic])


def remove_question(question_text):

    global ACTIVE_POOL

    ACTIVE_POOL = [
        q for q in ACTIVE_POOL
        if q["question"] != question_text
    ]

    print("QUESTION REMOVED:")
    print(question_text)

def add_question(question):

    ACTIVE_POOL.append(question)

    print("QUESTION ADDED:")
    print(question)


def topic_mastered(topic):

    if topic not in TOPIC_MASTERY:
        return False

    return TOPIC_MASTERY[topic] >= 3


def question_exists(question):

    return (
        question.strip()
        in
        GENERATED_QUESTIONS
    )


def remember_question(question):

    GENERATED_QUESTIONS.add(
        question.strip()
    )