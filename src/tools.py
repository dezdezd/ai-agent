import os
from tavily import TavilyClient

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query: str) -> str:
    try:
        results = tavily.search(query)
        parts = []

        for r in results['results'][:3]:
            parts.append(f"{r['title']}\n{r['content'][:300]}")

        return "\n\n".join(parts) if parts else "поиск не дал результатов"

    except Exception as e:
        return f"поиск недоступен: {e}"

def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"ошибка вычисления: {e}"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Searches internet for CURRENT or RECENT information: news, weather, prices, events. Do NOT use for historical facts, definitions, or well-known people.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query in English for best results"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculates math expressions. Use for any arithmetic, percentages, or numeric calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression, e.g. 2 + 2 or 50000 * 0.15"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]