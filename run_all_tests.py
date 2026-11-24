#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parent
failed = 0
passed = 0
for d in sorted(p for p in root.iterdir() if p.is_dir() and (p / "test_app.py").exists()):
    r = subprocess.run([sys.executable, "-m", "unittest", "test_app.py"], cwd=d, capture_output=True, text=True)
    if r.returncode == 0:
        passed += 1
        print(f"PASS  {d.name}")
    else:
        failed += 1
        print(f"FAIL  {d.name}\n{r.stderr}")
print(f"\nÖsszesen: {passed} sikeres, {failed} hibás.")
sys.exit(1 if failed else 0)
