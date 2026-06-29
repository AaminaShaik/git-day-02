import subprocess

process = subprocess.Popen(
    ["python", "hello.py"]
)
port = 2000
print(f"Python script started with PID: {process.pid}")
