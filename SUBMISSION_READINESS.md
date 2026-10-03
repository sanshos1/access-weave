# Submission readiness

| Requirement | Code path | Proof | Status |
| --- | --- | --- | --- |
| Accessibility need and constraints are frozen at creation | `chart_journey` | `ROUTE-1791054094` readback | PASS |
| Validators independently compare passage judgments | `prompt_comparative` in `propose_passage` | Three finalized accepted passages | PASS |
| Duplicate traveler and closed journey writes are rejected | deterministic guards in `propose_passage` | source test and deployed source match | PASS |
| Complete lifecycle reaches a terminal state | `IN_TRANSIT` to `ARRIVED` or `STRANDED` | `ARRIVED`, segment 3, zero barriers | PASS |
| Frontend waits for finality | `frontend/lib/chain.ts` | pinned build and browser readback | PASS |
| Submitted source matches deployment | deployment transaction source | byte-for-byte SHA-256 match | PASS |
| Canonical public site exposes the live state | Cloudflare Pages | three cleared segments visible in browser | PASS |

The live wallets are operator-controlled demo wallets and are not independent authorities. The contract decision is validator consensus over the frozen need, constraints, segment, and passage.
