from pathlib import Path

from app.ai.service import generate_content
import json


PROMPT_PATH = (
    Path(__file__).parent / "prompts" / "workout_prompt.txt"
)


def generate_workout(workout_request):
    with open(PROMPT_PATH, "r", encoding="utf-8") as file:
        base_prompt = file.read()

    user_prompt = f"""

User Information

Goal: {workout_request.goal}

Experience: {workout_request.experience}

Equipment: {workout_request.equipment}

Days Per Week: {workout_request.days_per_week}

Workout Duration: {workout_request.workout_duration} minutes

Injuries: {workout_request.injuries if workout_request.injuries else "None"}

Generate the workout plan.
"""

    final_prompt = base_prompt + "\n\n" + user_prompt

    response = generate_content(final_prompt)

# Remove markdown code blocks if Gemini adds them
    response = response.replace("```json", "").replace("```", "").strip()

    try:
        workout = json.loads(response)
        return workout
    except json.JSONDecodeError:
        return {
            "error": "Gemini returned invalid JSON",
            "raw_response": response,
        }