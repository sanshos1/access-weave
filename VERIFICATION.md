# Verification

The corrected contract passed four executable surface and consensus tests, GenVM lint, and semantic validation. Local source SHA-256 `0a9696524d35ccf85c1f728436ea32d58cd578f2c7cc7f335babd4c11fae7685` matches the decoded StudioNet deployment source byte-for-byte.

StudioNet finalized deployment `0xb7e0109a1931d7d5e39ecf6b114b77722bd00115a1058b953f0c13f488e5d3ee` with `MAJORITY_AGREE` and leader execution `SUCCESS`, producing contract `0x5563fC521Bc7dA579F9899bb03ED0d3b2bB1C408`.

Journey `ROUTE-1791054094` was created and completed by three distinct operator-controlled demo wallets. The creation and all three passage transactions finalized with `MAJORITY_AGREE` and `SUCCESS`. Canonical readback returned `ARRIVED`, current segment `3`, zero barriers, and three accepted attempts. These wallets demonstrate replay and unique-traveler behavior; they are not represented as independent authorities.

Cloudflare deployment `eba7f6ca` published the corrected build at https://sanshos1-access-weave.pages.dev/. Browser verification loaded the exact production URL and read the completed journey as three `CLEARED` segments, `ARRIVED`, and `0/3 BARRIERS`. The frontend waits for `FINALIZED` before refreshing state.

## Transaction record

- Create journey: `0x63b303e62cfd79f3872b5f47b6c8ad40c7ea4774176f5bcc90623b5827d5bba7`
- Passage 1: `0x8dc4200df0c23d023ab626fac9384d6579e669d788c86264fa419210b686e1c8`
- Passage 2: `0xd521da8aa15b95bcfac58aa1cc937b64931d8655c9dbdfa57c3bbb3ba12b3d5d`
- Passage 3: `0x5ea995003c5502e9d6564bffc1b41310a6ce0b1582cedc2f44b487191dba111e`
