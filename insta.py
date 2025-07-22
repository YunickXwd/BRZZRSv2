import platform
import os
import sys
import subprocess
import time

def typewriter(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def check_architecture():
    return platform.architecture()[0]

def git_pull():
    try:
        typewriter("🔁 Checking for updates via GitHub...", 0.02)
        subprocess.run(["git", "pull"], check=True)
        typewriter("✅ Updated successfully!\n", 0.02)
    except Exception as e:
        print("⚠️ Git pull failed:", e)

def run_main():
    try:
        import YunickInstaMain  # This loads the .so compiled module
    except ImportError as e:
        typewriter("❌ Failed to load tool: " + str(e))
        sys.exit(1)

def welcome_animation():
    banner = """
╔════════════════════════════════╗
║   🚀 Welcome to YunickXwd Tool 🚀   ║
╚════════════════════════════════╝
"""
    print(banner)
    typewriter("⚡ Tool created by: YunickXwd", 0.03)
    typewriter("📂 Running optimized Cython tool...", 0.03)
    typewriter("📱 Checking device architecture...", 0.03)

def main():
    os.system("clear" if os.name == "posix" else "cls")
    welcome_animation()
    arch = check_architecture()

    if '64' in arch:
        typewriter("✅ 64-bit device detected. Starting engine...\n", 0.03)
        git_pull()
        run_main()
    else:
        typewriter("❌ Sorry, your device is 32-bit. This tool supports only 64-bit devices.\n", 0.04)

if __name__ == "__main__":
    main()