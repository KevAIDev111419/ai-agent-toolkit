from litellm import completion
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content
