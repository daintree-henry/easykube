from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()
CONFIG_PATH = "/config/app.properties"

config = {}

def load_config_once():
    global config
    try:
        with open(CONFIG_PATH) as f:
            for line in f:
                if '=' in line:
                    k, v = line.strip().split('=', 1)
                    config[k] = v
    except Exception as e:
        print(f"[error] 설정 읽기 실패: {e}")

load_config_once()  # 실행 시 1회만 읽음

@app.get("/check", response_class=PlainTextResponse)
def get_config():
    if not config:
        return "⚠️ 설정 정보를 불러올 수 없습니다."

    lines = ["📄 현재 서비스 구성 상태:\n"]

    if "feature.debug" in config:
        if config["feature.debug"].lower() == "true":
            lines.append("✅ 디버그 모드가 활성화되어 있습니다.")
        else:
            lines.append("ℹ️ 디버그 모드는 비활성화되어 있습니다.")

    if "version" in config:
        lines.append(f"🔖 현재 서비스 버전은 {config['version']}입니다.")

    known_keys = {"feature.debug", "version"}
    others = {k: v for k, v in config.items() if k not in known_keys}
    for k, v in others.items():
        lines.append(f"🔸 {k} = {v}")

    return "\n".join(lines)