from litellm import completion
from typing import List, Dict

# 🧠 This function acts as a reusable wrapper to generate LLM responses.
# It helps standardize API access for agent-like behaviors.
# TODO: Extend this to support streaming or tool calling in future versions.

def generate_response(messages: List[Dict], model: str = "openai/gpt-4", max_tokens: int = 1024) -> str:
    """
    Generate a response from a Large Language Model using LiteLLM.

    Args:
        messages (List[Dict]): A list of message dictionaries in ChatML format.
            Each dictionary must contain:
            - "role": one of "system", "user", or "assistant"
            - "content": the text content for that role
        model (str): The model ID to use (default is GPT-4).
        max_tokens (int): The maximum number of tokens to generate (default 1024).

    Returns:
        str: The text content of the assistant's response.

    Example:
        >>> messages = [
        >>>     {"role": "system", "content": "You are a helpful assistant."},
        >>>     {"role": "user", "content": "What is the capital of France?"}
        >>> ]
        >>> generate_response(messages)
        'The capital of France is Paris.'
    """
    response = completion(
        model=model,
        messages=messages,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content
