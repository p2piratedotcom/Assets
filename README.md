# P2Pirate Assets

Versioned coin configuration, seed nodes, and the 453 previously used coin PNGs for the P2Pirate desktop wallet. The wallet asks before its first download and provides a manual **Check updates** action in Settings. The manifest protects every downloaded file with SHA-256; the Git commit identifies the full snapshot.

| Path | Purpose |
| --- | --- |
| `coins` | KDF coin definitions |
| `utils/coins_config_unfiltered.json` | SDK coin catalog |
| `seed-nodes.json` | KDF seed node data |
| `icons/*.png` | 453 restored coin icons |
| `manifest.json` | SHA-256 inventory |
| `tools/build_manifest.py` | SHA-256 manifest generator |

The initial JSON snapshot matches the P2Pirate GUI's reviewed build input from `ShorelineCrypto/coins` commit `98b29f5ea53a46a701e791a565a5fab7ee83b947`. The 453 PNG files also match the `icons/` directory at that source commit. These JSON files contain public network parameters and coin information. Future catalog changes should be reviewed as data changes before updating the manifest.

Refresh the manifest with Python 3 after changing any catalog or icon file:

```sh
python3 tools/build_manifest.py
```

The project owner states that they have permission to use the restored PNG artwork. The source repository does not publish a license for those PNGs; this README does not grant additional rights to them. See the [artwork notice](ARTWORK_NOTICE.md). [The Unlicense](LICENSE) applies only to P2Pirate-authored code in `tools/`. Coin and seed-node JSON are factual configuration data copied from the source commit above.

To check a snapshot locally, compare the SHA-256 of every file named in `manifest.json` against its entry. The wallet performs this check on download and keeps the last verified snapshot if a new download fails.
