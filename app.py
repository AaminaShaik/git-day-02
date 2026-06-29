import subprocess

process = subprocess.Popen(
    ["python", "hello.py"]
)

print(f"Python script started with PID: {process.pid}")
