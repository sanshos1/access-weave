# Access Weave

## Traveler card

Access Weave is a shared route rehearsal where every proposed passage must preserve a frozen accessibility need. Accepted passages advance the journey one segment. Unsafe workarounds consume one of three barrier strikes.

## Thread rules

The contract stores the need, constraints, ordered segments, unique travelers, progress, strikes, and terminal state. Deterministic guards reject closed journeys, duplicate travelers, and weak passages. GenLayer's comparative equivalence principle asks validators to agree on the access-preservation decision while allowing rationale wording to differ. Code advances exactly one segment or one strike, then derives `ARRIVED` or `STRANDED`.

Writes: `chart_journey`, `propose_passage`. Reads: `get_journey`, `get_attempts_page`, `get_journeys_page`, `get_summary`.

## Station checklist

```text
genvm-lint lint contracts/contract.py
python -m pytest tests/test_surface.py -q
cd frontend
npm install
npm run typecheck
npm run build
```

The static frontend reads StudioNet state before wallet connection and requests a browser wallet only for passages. This is a rehearsal tool, not certified accessibility or travel advice.

## Stamped route

- Contract: `0x5563fC521Bc7dA579F9899bb03ED0d3b2bB1C408`
- Deployment: `0xb7e0109a1931d7d5e39ecf6b114b77722bd00115a1058b953f0c13f488e5d3ee`
- Completed journey: `ROUTE-1791054094`
- Final passage: `0x5ea995003c5502e9d6564bffc1b41310a6ce0b1582cedc2f44b487191dba111e`
- Public station: https://access-weave.pages.dev/
