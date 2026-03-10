import sys

log_file = sys.argv[1]

with open(log_file, "r") as f:
    logs = f.read()

analysis = ""

if "ModuleNotFoundError" in logs:
    analysis = "Python dependency missing. Check requirements.txt"

elif "docker: command not found" in logs:
    analysis = "Docker is not installed in runner environment."

elif "ImagePullBackOff" in logs:
    analysis = "Kubernetes cannot pull image. Check DockerHub credentials or image tag."

elif "CrashLoopBackOff" in logs:
    analysis = "Application container crashed. Check application logs."

else:
    analysis = "Unknown error. Inspect pipeline logs."

print("\nAI FAILURE ANALYSIS")
print("--------------------")
print(analysis)
