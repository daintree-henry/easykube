import time
import threading

start_time = time.time()

def burn_cpu(target_usage=0.8, interval=1.0):
    busy_time = interval * target_usage
    idle_time = interval * (1 - target_usage)

    while True:
        elapsed = time.time() - start_time
        if 60 < elapsed < 360:  # 1분 뒤~6분까지 부하
            t0 = time.time()
            while (time.time() - t0) < busy_time:
                pass
            time.sleep(idle_time)
        else:
            time.sleep(0.5)  # 대기 모드

def main():
    threading.Thread(target=burn_cpu, daemon=True).start()
    while True:
        elapsed = int(time.time() - start_time)
        if 60 < elapsed < 360:
            print(f"[{elapsed}s] 🔥 CPU load ~80% running...")
        elif elapsed >= 360:
            print(f"[{elapsed}s] ✅ Back to normal mode")
        else:
            print(f"[{elapsed}s] ✅ Normal mode")
        time.sleep(5)

if __name__ == "__main__":
    main()
