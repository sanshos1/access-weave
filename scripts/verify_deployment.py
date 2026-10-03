import base64
import hashlib
import json
from pathlib import Path

from genlayer_py import create_client
from genlayer_py.chains import studionet


ROOT = Path(__file__).parents[1]
CONTRACT = "0x5563fC521Bc7dA579F9899bb03ED0d3b2bB1C408"
DEPLOYMENT_TX = "0xb7e0109a1931d7d5e39ecf6b114b77722bd00115a1058b953f0c13f488e5d3ee"
CLIENT = create_client(chain=studionet)
TX = CLIENT.get_transaction(transaction_hash=DEPLOYMENT_TX)
DEPLOYED = base64.b64decode(TX["data"]["contract_code"], validate=True)
LOCAL = (ROOT / "contracts" / "contract.py").read_text(encoding="utf-8").encode("utf-8")
LEADER = (TX.get("consensus_data", {}).get("leader_receipt") or [{}])[0]
REPORT = {
    "network": "StudioNet",
    "contract": CONTRACT,
    "deploymentTransaction": DEPLOYMENT_TX,
    "status": TX.get("status_name"),
    "consensus": TX.get("result_name"),
    "execution": LEADER.get("execution_result"),
    "sourceSha256": hashlib.sha256(DEPLOYED).hexdigest(),
    "sourceMatches": DEPLOYED == LOCAL,
}
assert TX.get("recipient", "").lower() == CONTRACT.lower()
assert REPORT["status"] == "FINALIZED"
assert REPORT["consensus"] == "MAJORITY_AGREE"
assert REPORT["execution"] == "SUCCESS"
assert REPORT["sourceMatches"] is True
(ROOT / "evidence" / "deployment-verification.json").write_text(
    json.dumps(REPORT, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(REPORT, indent=2), flush=True)
