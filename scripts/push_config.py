import time, pathlib, datetime

LOG = pathlib.Path("logs/pipeline.log")

print("Pushed .cli configs to spine/leaf (mock)")


def log_write(msg):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {msg}\n")

log_write("▶️ Starting push of configs...")
print("Applying base configs to nodes (mock)...")
time.sleep(2)
log_write("✅ Base config applied successfully")
print("✅ Base config applied successfully")

