import requests
import config


def ask_ai(prompt: str) -> str:
    try:
        response = requests.post(
            config.OLLAMA_URL,
            json={
                "model": config.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=90,
        )
        response.raise_for_status()
        answer = response.json().get("response", "").strip()
        return answer or "I could not generate an answer."
    except requests.RequestException as error:
        print("Ollama connection error:", error)
        return "My local AI service is not available right now."
