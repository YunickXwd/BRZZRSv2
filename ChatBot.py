import platform
import subprocess
import sys
import os
import time
import sys

def check_architecture():
    arch = platform.machine().lower()
    supported_archs = ['x86_64', 'amd64', 'aarch64', 'arm64']
    if arch in supported_archs:
        print(f"[INFO] Device architecture detected: {arch} — Supported ✅")
        return True
    else:
        print(f"[ERROR] Device architecture detected: {arch} — NOT Supported ❌")
        return False

def git_pull_update():
    if not os.path.exists(".git"):
        print("[WARN] No git repository found, skipping update.")
        return
    print("[INFO] Running git pull to update bot code...")
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True, check=True)
        print("[GIT PULL OUTPUT]")
        print(result.stdout)
        if "Already up to date." in result.stdout:
            print("[INFO] Bot is already up to date.")
        else:
            print("[INFO] Bot updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Git pull failed: {e.stderr}")

def loading_animation(message="Redirecting to bot", duration=3):
    print()
    print(message, end='', flush=True)
    for _ in range(duration * 3):  # multiply by 3 for 0.33s per dot for duration seconds
        print('.', end='', flush=True)
        time.sleep(0.33)
    print('\n')

def run_cython_bot():
    try:
        import BRZZRSbot
    except ImportError as e:
        print(f"[ERROR] Could not import BRZZRSbot module: {e}")
        sys.exit(1)

    if not hasattr(BRZZRSbot, "main"):
        print("[ERROR] BRZZRSbot module has no main() function.")
        sys.exit(1)

    print("[INFO] Starting BRZZRSbot...\n")
    BRZZRSbot.main()

def main():
    print("=== BRZZRSbot Launcher ===")
    if not check_architecture():
        print("Sorry, your device architecture is not supported by this bot.")
        sys.exit(1)

    git_pull_update()

    loading_animation("Redirecting to BRZZRSbot")

    run_cython_bot()

if __name__ == "__main__":
    main()