#!/usr/bin/env python3
"""
inject_pulse.py — drop a test pulse JSON into pulse-cache so the daemon picks it up.
Usage:  python inject_pulse.py [person]
"""
import json, os, sys, time

PULSE_DIR = os.environ.get("PULSE_CACHE", "./pulse-cache")
os.makedirs(PULSE_DIR, exist_ok=True)

person = sys.argv[1] if len(sys.argv) > 1 else "TestAgent"
pulse = {
    "person":      person,
    "timestamp":   time.strftime("%Y-%m-%dT%H:%M:%S"),
    "sensory":     "vision",
    "cue":         "garden breeze",
    "comment":     "Test pulse from inject_pulse.py",
    "age_seconds": 42
}

filename = os.path.join(PULSE_DIR, f"pulse_{person}_{int(time.time())}.json")
with open(filename, "w") as f:
    json.dump(pulse, f)

print(f"[INJECT] Wrote {filename}")
print(json.dumps(pulse, indent=2))
