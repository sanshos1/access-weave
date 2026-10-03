import json, re
from pathlib import Path
from genlayer_py import create_account, create_client
from genlayer_py.chains import studionet
from genlayer_py.types import TransactionStatus

ROOT = Path(__file__).parents[1]
env = (ROOT.parents[3] / "accounts.env").read_text()
key = re.search(r'^ACCOUNT_3_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', env, re.M).group(1).strip()
tx = __import__('sys').argv[1]
client = create_client(chain=studionet, account=create_account(account_private_key=key))
receipt = client.wait_for_transaction_receipt(transaction_hash=tx, status=TransactionStatus.FINALIZED, retries=180, interval=5000, full_transaction=True)
leader = (receipt.get("consensus_data", {}).get("leader_receipt") or [{}])[0]
address = receipt.get("data", {}).get("contract_address") or receipt.get("to_address")
print(json.dumps({"contract": address, "deploymentTx": tx, "status": receipt.get("status_name"), "consensus": receipt.get("result_name"), "execution": leader.get("execution_result"), "stderr": leader.get("stderr")}, default=str), flush=True)
