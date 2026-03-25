from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

from agent import run_agent

history = []

print("ассистент готов, напиши 'выход' чтобы закончить.\n")

while True:
    user_input = input("Ты: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "выход":
        break

    response = run_agent(history, user_input)
    print(f"Агент: {response}\n")