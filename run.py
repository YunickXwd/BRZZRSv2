import platform
import os
import sys
import time

def typewriter(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_bar(task, length=20, delay=0.05):
    print(f"⏳ {task}")
    bar = ""
    for i in range(length):
        bar += "█"
        print(f"\r[{bar:<{length}}] {int((i+1)/length*100)}%", end='', flush=True)
        time.sleep(delay)
    print("\n")

def check_architecture():
    loading_bar("Checking device architecture...")
    arch = platform.machine()
    if "64" in arch or arch == "aarch64":
        typewriter("\n✅ Device Supported (64-bit architecture detected)\n", 0.03)
        return True
    else:
        typewriter("\n❌ Device Not Supported\nThis tool only works on 64-bit devices.", 0.03)
        return False

def auto_update():
    typewriter("🔁 Checking for updates from GitHub...\n", 0.03)
    os.system("git pull")

def run_main():
    typewriter("🚀 Launching YunickMain Tool...", 0.03)
    time.sleep(1)
    try:
        import YunickMain
        YunickMain.main_menu()
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("➡️  Make sure YunickMain.cpython-312.so is in the same folder as run.py.")
        sys.exit(1)

if __name__ == "__main__":
    os.system("clear")
    typewriter("👑 Welcome to YunickXwd's BRZZRS v0.2", 0.04)
    print("-" * 45)
    auto_update()
    if check_architecture():
        run_main()