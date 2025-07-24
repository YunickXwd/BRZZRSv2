import os
import sys
import time
import requests
import platform
import subprocess
from itertools import cycle
from threading import Thread

def animate():
    for c in cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'\rChecking environment {c}')
        sys.stdout.flush()
        time.sleep(0.1)


def check_device():
    global done
    print("\n" + "="*50)
    print("Checking Device Compatibility...")
    
    if platform.system() != "Linux":
        print("\n[!] This tool only works on Android/Linux devices")
        return False
        
    machine = platform.machine()
    if "aarch64" in machine or "arm64" in machine:
        print("\n[✓] 64-bit Android Device Detected")
        return True
    else:
        print("\n[!] Sorry, 32-bit devices are not supported")
        return False

def update_tool():
    print("\n" + "="*50)
    print("Checking for updates...")
    try:
        output = subprocess.check_output(["git", "pull"]).decode()
        if "Already up to date" in output:
            print("[✓] Tool is already up-to-date")
        else:
            print("[✓] Tool updated successfully")
            print(output)
    except Exception as e:
        print(f"[!] Update failed: {str(e)}")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    global done
    done = False
    t = Thread(target=animate)
    t.start()
    
    time.sleep(2) 
    done = True
    
    if not check_device():
        sys.exit(1)
        
    update_tool()
    
    print("\n" + "="*50)
    print("Starting Facebook UID Dumper...\n")
    
    try:
        from YunickDump import FacebookUIDDumper
        dumper = FacebookUIDDumper()
        dumper.run()
    except ImportError:
        print("[!] Error: Could not load compiled module")
        print("[!] Make sure YunickDump.cpython-312.so is in the same directory")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()