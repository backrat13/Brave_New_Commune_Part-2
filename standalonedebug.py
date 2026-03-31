import os
from pathlib import Path

def pre_flight_permissions_check(root_path):
    print("\n[SYSTEM] Running Substrate Integrity Check...")
    data_path = Path(root_path).expanduser() / "data"
    agents = ["sara", "art", "hel", "echo", "mira", "codex"]
    sub_dirs = ["axioms", "diary"]
    
    issues = 0
    for agent in agents:
        for sub in sub_dirs:
            target_dir = data_path / sub / agent
            if not target_dir.exists():
                continue
                
            # Attempt to create/append to a dummy file to test 'Errno 13'
            test_file = target_dir / "permissions_test.tmp"
            try:
                with open(test_file, "a") as f:
                    f.write("test")
                os.remove(test_file)
            except PermissionError:
                print(f"!! PERMISSION DENIED: {target_dir}")
                issues += 1
            except Exception as e:
                print(f"!! SYSTEM ERROR on {agent}/{sub}: {e}")
                issues += 1
                
    if issues == 0:
        print("[SYSTEM] Substrate is writable. All agents have clearance to breathe.\n")
        return True
    else:
        print(f"\n[FATAL] Found {issues} permission blocks. Run the 'chown' bash commands first.")
        return False

# Usage inside main():
# if not pre_flight_permissions_check(args.root):
#     sys.exit(1)
