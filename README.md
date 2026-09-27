# Access Weave

## Traveler card

Access Weave is a shared route rehearsal where every proposed passage must preserve a frozen accessibility need. Accepted passages advance the journey one segment. Unsafe workarounds consume one of three barrier strikes.

## Thread rules

The contract stores the need, constraints, ordered segments, unique travelers, progress, strikes, and terminal state. Deterministic guards reject closed journeys, duplicate travelers, and weak passages. Validators judge substantive equivalence against every stored constraint. Code advances exactly one segment or one strike, then derives `ARRIVED` or `STRANDED`.

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

- Contract: `0x2dE16c7084760Bc3CDf4C0999f2e30a2D0934B10`
- Deployment: `0xf5d7680aa109d13eca0c2118e11ea20cf3c6bc5979f252fbd506b13ee49435d5`
- Public station: https://sanshos1-access-weave.pages.dev/
