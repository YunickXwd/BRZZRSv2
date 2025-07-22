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
        typewriter("✅ Git updated successfully!\n", 0.02)
    except Exception as e:
        print("⚠️ Git pull failed:", e)

def run_main():
    try:
        import YunickInstaMain
        YunickInstaMain.main()  # 🔥 Call your main() function here
    except ImportError as e:
        typewriter("❌ Import Error: " + str(e))
        sys.exit(1)
    except AttributeError:
        typewriter("❌ Error: main() function not found in compiled module.")
        sys.exit(1)

def welcome_animation():
    banner = """
╔══════════════════════════════════════════╗
║    🚀 Welcome to YunickXwd Insta Tool 🚀    ║
╚══════════════════════════════════════════╝
"""
    print(banner)
    typewriter("🔒 Instagram Cracking Tool | By YunickXwd", 0.03)
    typewriter("💻 Compiled & Optimized with Cython", 0.03)
    typewriter("📲 Starting environment checks...\n", 0.03)

def main():
    os.system("clear" if os.name == "posix" else "cls")
    welcome_animation()
    arch = check_architecture()

    if '64' in arch:
        typewriter("✅ 64-bit device detected. Launching tool...\n", 0.03)
        git_pull()
        run_main()
    else:
        typewriter("❌ Sorry, your device is 32-bit. This tool only runs on 64-bit systems.\n", 0.04)

if __name__ == "__main__":
    main()