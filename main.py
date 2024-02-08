import subprocess

# List of scripts to run
scripts = ['hue_controller.py', 'recorder.py', 'transcriber.py', 'sentiment.py']

# Function to run a script concurrently
def run_script(script_name):
    try:
        subprocess.Popen(['python', script_name])
    except Exception as e:
        print(f"Failed to start script '{script_name}': {e}")

# Start each script concurrently
for script in scripts:
    run_script(script)