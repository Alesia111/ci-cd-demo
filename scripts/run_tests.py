import datetime, pathlib, time

LOG = pathlib.Path("logs/pipeline.log")

def log_write(msg):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {msg}\n")

log_write("▶️ Starting validation tests...")

# Simulo ping
time.sleep(1)
ping_result = "PING 172.20.20.4: time=4.5 ms"
print(ping_result)
log_write(ping_result)

# Simulo show interface
iface_result = "show interface brief -> eth1 UP, eth2 UP"
print(iface_result)
log_write(iface_result)

# Simulo show evpn
evpn_result = "show evpn -> 2 MAC routes installed"
print(evpn_result)
log_write(evpn_result)

log_write("✅ Validation completed successfully")
print("✅ Validation completed successfully")

