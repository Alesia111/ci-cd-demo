import yaml, pathlib, sys, datetime

LOG = pathlib.Path("logs/pipeline.log")

def log_write(msg):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {msg}\n")

try:
    path = pathlib.Path("topology/evpn01.yml")
    data = yaml.safe_load(path.read_text())
    nodes = data.get("nodes", [])
    log_write(f"✅ Precheck OK - Found {len(nodes)} nodes")
    print(f"✅ Precheck OK - Found {len(nodes)} nodes")
except Exception as e:
    log_write(f"❌ Precheck failed: {e}")
    print(f"❌ Precheck failed: {e}")
    sys.exit(1)

