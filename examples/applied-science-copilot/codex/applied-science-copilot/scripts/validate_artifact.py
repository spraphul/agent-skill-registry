#!/usr/bin/env python3
import json, sys
from pathlib import Path

if len(sys.argv) < 2:
    raise SystemExit("usage: validate_artifact.py ARTIFACT_JSON")
path = Path(sys.argv[1])
json.loads(path.read_text())
print(f"ok: {path}")
