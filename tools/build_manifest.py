#!/usr/bin/env python3
"""Write a reproducible SHA-256 inventory for the downloadable asset set."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    paths = [ROOT / "coins", ROOT / "seed-nodes.json", ROOT / "utils/coins_config_unfiltered.json"]
    paths += sorted((ROOT / "icons").glob("*.png"))
    files = {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
    }
    manifest = {"schema": 1, "icon_count": len(paths) - 3, "sha256": files}
    (ROOT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Wrote manifest for {len(files)} files")


if __name__ == "__main__":
    main()
