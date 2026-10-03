import json
import re
import time
from pathlib import Path

from genlayer_py import create_account, create_client
from genlayer_py.chains import studionet
from genlayer_py.types import TransactionStatus


ROOT = Path(__file__).parents[1]
ENV = (ROOT.parents[3] / "accounts.env").read_text(encoding="utf-8")
ADDRESS = "0x5563fC521Bc7dA579F9899bb03ED0d3b2bB1C408"


def account(number: int):
    private_key = re.search(
        rf'^ACCOUNT_{number}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', ENV, re.M
    ).group(1).strip()
    return create_account(account_private_key=private_key)


def client(number: int):
    return create_client(chain=studionet, account=account(number))


def finalized_write(number: int, function_name: str, args: list):
    active = client(number)
    tx = active.write_contract(address=ADDRESS, function_name=function_name, args=args)
    print(function_name + "_tx=" + str(tx), flush=True)
    receipt = active.wait_for_transaction_receipt(
        transaction_hash=tx,
        status=TransactionStatus.FINALIZED,
        retries=180,
        interval=5000,
        full_transaction=True,
    )
    leader = (receipt.get("consensus_data", {}).get("leader_receipt") or [{}])[0]
    if receipt.get("result_name") != "MAJORITY_AGREE" or leader.get("execution_result") != "SUCCESS":
        raise RuntimeError({"transaction": str(tx), "consensus": receipt.get("result_name"), "leader": leader})
    return {
        "transaction": str(tx),
        "status": "FINALIZED",
        "consensus": receipt.get("result_name"),
        "execution": leader.get("execution_result"),
        "explorer": "https://explorer-studio.genlayer.com/transactions/" + str(tx),
    }


journey_id = "ROUTE-" + str(int(time.time()))
need = "A wheelchair user must move from the street entrance to the boarding point without stairs, gaps, or reduced wayfinding."
constraints = [
    "No stairs or step-only transitions",
    "Maintain a continuous firm route at least 1.2 meters wide",
    "Provide equivalent visual and tactile wayfinding at every decision point",
]
segments = [
    "Street entrance to ticket hall",
    "Ticket hall to platform access",
    "Platform access to boarding point",
]
passages = [
    "Use the level east entrance, a 1.4 meter firm corridor, automatic doors, and matching tactile and high-contrast signs to reach the ticket hall without steps.",
    "Continue from the ticket hall through the staffed wide gate to the elevator; the 1.3 meter firm route has tactile and high-contrast direction signs at each turn.",
    "Exit the elevator onto the level platform and follow a 1.4 meter unobstructed tactile-marked corridor with visual signs to the level boarding point.",
]

transactions = [finalized_write(3, "chart_journey", [journey_id, need, constraints, segments])]
for wallet_number, passage in zip([1, 2, 4], passages):
    transactions.append(finalized_write(wallet_number, "propose_passage", [journey_id, passage]))

reader = client(3)
state = reader.read_contract(address=ADDRESS, function_name="get_journey", args=[journey_id])
attempts = reader.read_contract(address=ADDRESS, function_name="get_attempts_page", args=[journey_id, 0, 20])
if state.get("state") != "ARRIVED" or state.get("current") != 3 or state.get("strikes") != 0:
    raise RuntimeError({"state": state, "attempts": attempts})

proof = {
    "network": "StudioNet",
    "contract": ADDRESS,
    "journeyId": journey_id,
    "walletDisclosure": "All wallets in this rehearsal are operator-controlled demo wallets, not independent third parties.",
    "transactions": transactions,
    "state": state,
    "attempts": attempts,
}
(ROOT / "evidence").mkdir(exist_ok=True)
(ROOT / "evidence" / "live-journey.json").write_text(json.dumps(proof, indent=2), encoding="utf-8")
print(json.dumps(proof, indent=2), flush=True)
