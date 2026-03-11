import os
import sys
from openai import OpenAI

try:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    log_text = sys.stdin.read()

    prompt = f"""
    Analyze this CI/CD failure and explain root cause and fix:

    {log_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    print("\nAI FAILURE ANALYSIS")
    print(response.choices[0].message.content)

except Exception as e:
    print("\nAI Analyzer could not run.")
    print("Possible reason: OpenAI quota exceeded or API issue.")
    print("Fallback suggestion: Check Docker build logs and dependency errors.")
