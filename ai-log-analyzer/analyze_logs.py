import os
import sys
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

log_file = sys.argv[1]

with open(log_file, "r") as f:
    logs = f.read()

prompt = f"""
You are a DevOps assistant.

Analyze the following CI/CD pipeline logs and explain:
1. Root cause of failure
2. Suggested fix

Logs:
{logs}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print("\nAI FAILURE ANALYSIS")
print("--------------------")
print(response.choices[0].message.content)
