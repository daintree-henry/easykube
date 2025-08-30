from flask import Flask, request
import time, threading, sys, os

app = Flask(__name__)
boot_time = time.time()
last_state = None
current_state = None  

MODE = os.getenv("MODE", "success")  

def get_state():
    if MODE == "fail-startup":
        return "Startup"   
    if MODE == "fail-readiness":
        return "Warmup"    
    if MODE == "fail-liveness":
        return "Failing"   

    # success 모드: 시간 기반 상태머신
    elapsed = time.time() - boot_time
    if elapsed < 60:
        return "Startup"
    elif elapsed < 80:
        return "Warmup"
    elif elapsed < 140:
        return "Running OK"
    else:
        return "Failing"

def background_logger():
    global last_state, current_state
    while True:
        state = get_state()
        if state != last_state:
            elapsed = time.time() - boot_time
            print(f"[{elapsed:.1f}s] State changed -> {state}", file=sys.stderr, flush=True)
            last_state = state
        current_state = state
        time.sleep(1)

threading.Thread(target=background_logger, daemon=True).start()

def log_request(endpoint, result):
    elapsed = time.time() - boot_time
    print(f"[{elapsed:.1f}s] {endpoint} -> {result}", file=sys.stderr, flush=True)

@app.route("/startupz")
def startup():
    if current_state == "Startup":
        log_request("/startupz", "FAIL")
        return "Starting...", 500
    log_request("/startupz", "OK")
    return "Started", 200

@app.route("/readyz")
def ready():
    if current_state in ["Startup", "Warmup"]:
        log_request("/readyz", "FAIL")
        return "Not Ready", 500
    log_request("/readyz", "OK")
    return "Ready", 200

@app.route("/healthz")
def health():
    if current_state in ["Startup", "Warmup"]:
        log_request("/healthz", "FAIL (not ready yet)")
        return "Not Ready Yet", 500
    if current_state == "Running OK":
        log_request("/healthz", "OK")
        return "Healthy", 200
    if current_state == "Failing":
        log_request("/healthz", "FAIL")
        return "Failing after timeout", 500
    return "Unexpected", 500

@app.route("/")
def index():
    return "Hello from Probe Demo!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
