# 🧠 Agent Workflow: Code → Docs → Tests (3-Phase Prompt Strategy)

This document outlines how to sequence an LLM through three structured phases of function development using prompt memory.

---

## ✅ Phase 1: Initial Code Generation

```python
messages = [
    {"role": "system", "content": "You are a Python expert helping to develop a function."}
]

messages.append({
    "role": "user",
    "content": f"Write a Python function that {function_description}. Output the function in a ```python code block```."
})

## ✅ Phase 2: Documentation Enhancement

messages.append({
    "role": "assistant", 
    "content": "```python\n\n" + initial_function + "\n\n```"
})

messages.append({
    "role": "user",
    "content": "Add comprehensive documentation to this function..."
})

## ✅ Phase 3: Test Case Generation

messages.append({
    "role": "assistant", 
    "content": "```python\n\n" + documented_function + "\n\n```"
})

messages.append({
    "role": "user",
    "content": "Add unittest test cases for this function..."
})
