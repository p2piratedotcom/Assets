# Assets: AI and contributor project guide

Read [AGENTS.md](../AGENTS.md) first. Facts were checked on 2026-10-06 against
its source revision. This repository is a public data/artwork snapshot, not a
wallet program, credential store, KDF binary or trading engine.

## Role and consumers

The [wallet](https://github.com/p2piratedotcom/P2Pirate-ALPHA/blob/cheetahdex/AGENTS.md)
asks before downloading a commit-pinned snapshot, verifies payload paths/sizes/
hashes, and stages activation. The [SDK](https://github.com/p2piratedotcom/komodo-defi-sdk-flutter/blob/cheetahdex/AGENTS.md)
parses/uses the catalog and icon directory according to the wallet's update policy.
[MM_Engine](https://github.com/p2piratedotcom/MM_Engine/blob/main/AGENTS.md)
receives the wallet's coin registry; it does not obtain funding/risk authority
from these JSON files. [CEX plugins](https://github.com/p2piratedotcom/CEX_configs/blob/main/AGENTS.md)
have their own executable catalog and separate exchange mappings.

A new Git commit is a new repository snapshot, but not automatic replacement of
a running wallet's catalog. The wallet retains verified snapshots/offline fallback;
manual downloads during a running session activate under its documented restart
policy. Tor-mode KDF bootstrap uses its bundled node path in the reviewed wallet;
this repo's node data is not proof that every consumer uses it in every mode.
Inspect the wallet/SDK source when diagnosing connectivity.

## Payload map and schema

| File | Content and invariants |
| --- | --- |
| `coins` | JSON list of KDF coin definitions; protocol/network/confirmations and endpoint parameters |
| `utils/coins_config_unfiltered.json` | JSON object keyed by coin config IDs with SDK names, flags, providers/explorer metadata and protocol information |
| `seed-nodes.json` | Public bootstrap hosts and metadata such as domain type, WSS and NetID |
| `icons/*.png` | Existing artwork files; separate rights/provenance apply |
| `manifest.json` | Schema 1, `icon_count`, `sha256` map of exact payload-relative paths |
| `tools/build_manifest.py` | Reproducible inventory generator |
| `ARTWORK_NOTICE.md`, `LICENSE`, `README.md` | Provenance and scoped rights, not wallet payload |

At this reviewed snapshot the two coin inputs contain 750 entries and the manifest
records 453 PNGs. Those are dated inventory counts, **not** a promise of 750
supported/activatable/tradable chains. Derive current counts from data/manifest.
Config IDs can encode chain variants and case-sensitive suffixes; do not flatten
variants by a ticker or guess a CEX Spot mapping from one.

The initial coin/node inputs and restored artwork are traced to the source commit
in [README.md](../README.md). Public network data is different from a secret
wallet recovery phrase. Never add wallet/account secrets, API credentials,
private endpoints or a private funded profile to public data.

## Integrity and trust model

The generator inventories exactly `coins`, `seed-nodes.json`,
`utils/coins_config_unfiltered.json` and sorted PNG files. It hashes bytes, writes
sorted JSON keys and calculates icon count. A whitespace/data edit changes the
payload digest even if its meaning is similar. Keep schema/path names compatible
with consumers; a new payload type is a consumer/schema change, not just another
manifest entry.

SHA-256 checks establish content consistency against the chosen repository
snapshot. They are not an independent publisher signature or proof an endpoint,
coin definition or logo is trustworthy. Review RPC/explorer/node replacements,
TLS/host semantics, protocol/network IDs and changed support flags as meaningful
security/compatibility changes. Valid JSON is not funded chain acceptance.

The wallet accepts its known payload allowlist and checks manifest/archive
agreement before staging it. AGENTS/docs/PR templates are repository guidance,
not entries to add to the payload hash map. Docs-only changes do not need a
manifest rewrite and do not change payload hashes, even though Git HEAD changes.

## Safe editing and validation workflow

1. Identify the intended config ID/network and both KDF/SDK representations.
   Establish endpoint/source provenance; inspect consumer compatibility before
   adding/removing fields or changing chain/token semantics.
2. Keep JSON types, explicit protocol data and identifiers consistent. Adding an
   image does not itself add support; removing it should retain safe UI fallback.
3. Review rights and attribution for artwork/data before adding files. Do not
   invent distribution permission from the extension, old inclusion or checksum.
4. After a payload edit, regenerate and commit payload plus manifest together:

```sh
python3 tools/build_manifest.py
```

5. Inspect the diff and independently compare every manifest-listed file's bytes
   to its SHA-256, path set and icon count. Review semantic data correctness too;
   a generator cannot validate chain behavior or authorize funds.
6. Use disposable consumers for any activation/integration check. Do not upgrade
   a real wallet catalog or change live endpoints merely to verify documentation.

There is currently no checked-in CI workflow or dedicated test suite in this
repo. A PR with no checks is not a validated data change. Documentation-only
publication can be checked for source accuracy/links without running the generator
or contacting nodes. Never report runtime/chain/funded checks that were not done.

## Artwork and licenses

Read [ARTWORK_NOTICE.md](../ARTWORK_NOTICE.md). The owner has stated permission
for restored artwork, but no general permission document is published there.
The repository's Unlicense applies to P2Pirate-authored tooling, not the PNGs.
Their presence/checksums do not give external contributors an unrestricted reuse
license. Keep source attribution and review new rights separately. Wallet binary
recipes can deliberately exclude artwork even when the optional asset snapshot
contains it; do not assume one distribution policy covers the other.

## Where a fix belongs

- Coin/node/icon payload and manifest: this repository.
- Download consent, verification, archive/path limits, active pointer and restart
  policy: wallet `lib/services/coin_assets/`.
- Parsing, runtime icon selection, coin updater/platform behavior: SDK packages.
- Maker availability, CEX minimums, hedge funding and strategy budgets: MM_Engine.
- Native exchange aliases, permissions and signing: CEX_configs.
- KDF chain implementation: external Rust KDF, not this catalog.

When an asset cannot activate, separate bad configuration, unavailable endpoint,
wrong network/parameters, runtime version, route and wallet state. Do not mark
it supported or relax validation solely to suppress an error. Metadata flags are
not automatic permission to trade or a guarantee of chain compatibility.

## A safe starting prompt for an AI contributor

```text
Read AGENTS.md and docs/AI_PROJECT_GUIDE.md at this checkout's revision.
My task is: [describe the requested change].
Identify the component boundary, relevant source/contracts, current limitations,
validation appropriate to this scope, and whether these guides need updating.
Use disposable fixtures; do not start a real wallet/service or submit funded
operations without the operator's explicit authorization.
Report facts separately from assumptions and checks performed from checks not run.
```

## Maintenance and PR handoff

Recheck this guide and `AGENTS.md` in the same PR when architecture, public
contracts, ownership, safety, persistence, routing, supported platforms,
dependencies, setup/tests, generated outputs, provenance or acceptance limits
change. Update linked specifications too when their contract changed. The PR
maintenance checklist requires either the corresponding edits or an explicit
no-update reason; a checkbox alone does not make an old statement true.

Keep version claims dated and tied to source/release evidence. Do not copy a local
runtime path, user account, balance, API credential or private monitoring result
into public guidance. Prefer links to manifests/constants over repeated moving
pins or exhaustive API copies. A cross-repository change needs companion PRs and
compatibility notes; do not assume that merging one repo deploys the whole system.

A useful AI handoff states: repository and commit, requested scope, relevant
modules/contracts, proposed change, risks, exact checks actually performed,
checks not run, companion repositories affected, and guide sections updated.
Implementation, fixture tests, a compatible release, installation, startup,
read-only account validation and funded acceptance are separate milestones.
