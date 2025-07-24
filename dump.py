import platform
import subprocess
import sys

def is_64bit():
    return platform.machine().endswith('64')

def git_pull():
    try:
        print("🔄 Pulling latest updates from Git...")
        subprocess.run(['git', 'pull'], check=True)
    except subprocess.CalledProcessError:
        print("❌ Git pull failed.")
        sys.exit(1)

def main():
    if not is_64bit():
        print("❌ Your device is not 64-bit. This tool only supports 64-bit systems.")
        sys.exit(1)

    git_pull()

    print("🚀 Starting YunickFileDump Tool...")
    try:
        import YunickDump
        YunickDump.main() 
    except AttributeError:
        print("✅ Module imported, but no main() function found. If your code runs on import, you're good.")
    except ImportError as e:
        print(f"❌ Failed to import YunickDump: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()