import re
from typing import List

STOPWORDS = {
    "para",
    "com",
    "uma",
    "por",
    "que",
    "como",
    "em",
    "de",
    "do",
    "da",
    "dos",
    "das",
    "um",
    "o",
    "a",
    "os",
    "as",
    "e",
    "no",
    "na",
    "nos",
    "nas",
    "se",
    "ao",
    "à",
    "às",
    "é",
    "ser",
    "ter",
    "quero",
    "situação",
    "bloqueios",
    "intenção",
}


def analyze_intentions(goal: str) -> List[str]:
    """Extrai intenções-chave por heurística simples para uso local."""
    cleaned = re.sub(r"[^\w\sáéíóúàâêôãõç-]", " ", goal.lower())
    words = [word.strip("-") for word in cleaned.split() if word]
    keywords = [word for word in words if word not in STOPWORDS and len(word) > 3]

    unique_keywords = []
    for word in keywords:
        if word not in unique_keywords:
            unique_keywords.append(word)

    if not unique_keywords:
        return ["clareza do objetivo", "organização das próximas ações"]

    return [f"Foco em {keyword}" for keyword in unique_keywords[:5]]
