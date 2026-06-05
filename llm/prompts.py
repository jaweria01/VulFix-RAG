# llm/prompts.py

SECURITY_PATCH_PROMPT = """
You are an expert software security engineer.

Your task is to repair vulnerable code.

Vulnerability Type:
{vulnerability}

Security Guidance:
{knowledge}

Vulnerable Code:
{code}

Requirements:
1. Fix the vulnerability.
2. Preserve functionality.
3. Return only the patched code.
4. Do not explain your answer.
"""