from fastapi import APIRouter

from app.models.schemas import StudentAnswer

from app.services.ai_service import generate_variants

from app.services.quiz_state import (
    reset_quiz,
    get_random_question,
    increase_mastery,
    decrease_mastery,
    remove_question,
    add_question,
    topic_mastered,
    question_exists,
    remember_question,
    ACTIVE_POOL
)

router = APIRouter(prefix="/student")


@router.post("/start")
def start_quiz():

    reset_quiz()

    question = get_random_question()

    return {
        "question": question
    }


@router.get("/question")
def get_question():

    question = get_random_question()

    if not question:

        return {
            "completed": True
        }

    return {
        "completed": False,
        "question": question
    }


@router.post("/answer")
def answer_question(answer: StudentAnswer):

    is_correct = (
        answer.student_answer.strip()
        ==
        answer.correct_answer.strip()
    )

    topic = answer.topic

    if is_correct:

        increase_mastery(topic)

        remove_question(answer.question)

        if topic_mastered(topic):

            remove_topic(topic)

            print(f"{topic} MASTERED")

    else:

        decrease_mastery(topic)

        variants = generate_variants(
            answer.question,
            topic
        )

        for variant in variants:

            add_question({
                "topic": topic,
                "question": variant["question"],
                "answer": variant["answer"]
            })

    print("ACTIVE_POOL:")
    print(ACTIVE_POOL)

    next_question = get_random_question()

    return {
        "correct": is_correct,
        "next_question": next_question,
        "completed": next_question is None
    }