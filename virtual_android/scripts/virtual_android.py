import subprocess
import time
import psutil

AVD_NAME = "Pixel_4_API_30"
APK_PATH = "sample_app.apk"

def start_emulator():
    print("[*] Starting Android Emulator...")
    subprocess.Popen(["emulator", "-avd", AVD_NAME])
    time.sleep(30)  # Wait for emulator to boot

def install_apk():
    print("[*] Installing APK...")
    subprocess.run(["adb", "install", APK_PATH])

def get_system_info():
    print("[*] Fetching system info...")
    os_version = subprocess.getoutput("adb shell getprop ro.build.version.release")
    device_model = subprocess.getoutput("adb shell getprop ro.product.model")
    memory_info = subprocess.getoutput("adb shell cat /proc/meminfo | grep MemTotal")

    print(f"OS Version: {os_version}")
    print(f"Device Model: {device_model}")
    print(f"Available Memory: {memory_info}")

    with open("system_info.log", "w") as f:
        f.write(f"OS Version: {os_version}\n")
        f.write(f"Device Model: {device_model}\n")
        f.write(f"Available Memory: {memory_info}\n")

def kill_emulator():
    print("[*] Stopping Emulator...")
    subprocess.run(["adb", "emu", "kill"])

if __name__ == "__main__":
    start_emulator()
    install_apk()
    get_system_info()
    kill_emulator()
    print("[✓] Virtual Android Simulation Completed!")
