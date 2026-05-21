import requests
import json
import re
import random

from app.core.config import (
    AI_API_URL,
    AI_API_KEY,
    AI_MODEL
)

from app.services.quiz_state import question_exists

from app.services.topic_definitions import (
    TOPIC_DEFINITIONS
)

def extract_json_array(text):

    match = re.search(
        r"\[[\s\S]*?\]",
        text
    )

    if match:
        return match.group(0)

    return None


def generate_local_fallback(question):

    print("USING LOCAL FALLBACK GENERATION")

    attempts = 0

    while attempts < 20:

        a = random.randint(1, 10)
        b = random.randint(1, 10)

        if "+" in question:

            new_question = f"{a} + {b} = ?"

            if (
                new_question != question
                and
                not question_exists(new_question)
            ):

                return [{
                    "question": new_question,
                    "answer": str(a + b)
                }]

        elif "-" in question:

            new_question = f"{a} - {b} = ?"

            if (
                new_question != question
                and
                not question_exists(new_question)
            ):

                return [{
                    "question": new_question,
                    "answer": str(a - b)
                }]

        attempts += 1

    return []


def generate_variants(question, topic):

    topic_data = TOPIC_DEFINITIONS.get(topic)

    description = topic_data["description"]

    examples = "\n".join(
        topic_data["examples"]
    )
    
    prompt = f"""
    Generate 1 (one) UNIQUE math exercise.

    Topic description:
    {description}

    Examples:
    {examples}

    Original:
    {question}

    Rules:
    - Keep same learning objective
    - Keep same difficulty
    - Must be different (do NOT give the same question as original)
    - Return ONLY valid JSON
    - No markdown
    - No explanations nor additional text other than the JSON

    Format:
    [
    {{
        "question": "...",
        "answer": "..."
    }}
    ]
    """

    try:

        response = requests.post(
            AI_API_URL,
            headers={
                "Authorization": f"Bearer {AI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": AI_MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You generate arithmetic exercises in JSON only."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.5,
                "max_tokens": 500
            },
            timeout=20
        )

        data = response.json()

        print("FULL HF RESPONSE:")
        print(data)

        if "error" in data:

            print("HUGGING FACE ERROR:")
            print(data["error"])

            return generate_local_fallback(question)

        raw_text = (
            data["choices"][0]["message"]["content"]
        )

        print("RAW AI RESPONSE:")
        print(raw_text)

        json_text = extract_json_array(raw_text)

        if not json_text:

            print("NO JSON FOUND")

            return generate_local_fallback(question)

        parsed = json.loads(json_text)

        normalized = []

        for item in parsed:

            ai_question = (
                item.get("question")
                or item.get("equation")
            )

            ai_answer = (
                item.get("answer")
                or item.get("solution")
            )

            if (
                ai_question
                and
                ai_answer is not None
            ):

                ai_question = str(ai_question).strip()

                if (
                    ai_question == question.strip()
                    or
                    question_exists(ai_question)
                ):
                    continue

                normalized.append({
                    "question": ai_question,
                    "answer": str(ai_answer)
                })

        if len(normalized) == 0:

            print("AI GENERATED DUPLICATES")

            return generate_local_fallback(question)

        print("USING AI GENERATED VARIANT")

        print("NORMALIZED VARIANTS:")
        print(normalized)

        return normalized

    except Exception as e:

        print("AI GENERATION FAILED:")
        print(e)

        return generate_local_fallback(question)