import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "store", "company.json")


def load_data():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_context(question: str):
    data = load_data()

    question = question.lower()

    relevant_parts = []

    for item in data:
        text = (item["title"] + " " + item["content"]).lower()

        # простая проверка релевантности
        if any(word in text for word in question.split()):
            relevant_parts.append(item)

    # если ничего не найдено
    if not relevant_parts:
        return None

    context = ""
    for item in relevant_parts:
        context += item["title"] + "\n"
        context += item["content"] + "\n\n"

    return context