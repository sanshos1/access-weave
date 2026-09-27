from pathlib import Path
R=Path(__file__).parents[1];S=(R/'contracts'/'contract.py').read_text()
def test_surface():
 assert S.startswith('# { "Depends": "py-genlayer:') and 'run_nondet_unsafe' in S and 'emit_transfer' not in S
 for x in('chart_journey','propose_passage','get_attempts_page','get_journeys_page'):assert f'def {x}'in S
def test_docs():
 for x in('README.md','PRODUCT_BOUNDARY.md','frontend-design-contract.md','readme-design-contract.md','VERIFICATION.md'):assert(R/x).exists()
