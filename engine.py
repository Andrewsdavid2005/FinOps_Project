import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta

# --- 1. SMART CONTRACT RULES (Policy Engine) ---
def apply_smart_contracts(row):
    """
    Simulates an Enterprise-grade Smart Contract Rule Engine.
    Rules are immutable once deployed to the engine.
    """
    status = "Approved"
    flags = []

    # Rule A: Spending Cap Policy
    if row['amount'] > 4500:
        status = "Flagged"
        flags.append("CAP_EXCEEDED: Transaction > $4,500")

    # Rule B: Shadow IT Detection (Unapproved Vendor-Dept pairs)
    shadow_it_map = {'Sales': 'AWS', 'HR': 'GitHub', 'Marketing': 'Docker'}
    if shadow_it_map.get(row['department']) == row['vendor']:
        status = "Flagged"
        flags.append("SHADOW_IT: Unauthorized Vendor for Department")

    # Rule C: Duplicate Tooling Detection
    if row['vendor'] in ['Zoom', 'Slack'] and row['amount'] > 3000:
        status = "Flagged"
        flags.append("DUPLICATE_TOOL: High spend on non-standard comms")

    return status, " | ".join(flags) if flags else "Policy Compliant"

# --- 2. DATA INGESTION & NORMALIZATION ---
def ingest_data():
    """
    Simulates ingestion from ERP, Cloud (AWS/GCP), and SaaS feeds.
    Normalizes data into a single schema.
    """
    depts = ['Engineering', 'Marketing', 'Sales', 'HR', 'Operations']
    vendors = ['AWS', 'Google Cloud', 'Zoom', 'Slack', 'GitHub', 'Oracle']
    projects = ['Alpha', 'Internal-Ops', 'Customer-Portal', 'AI-R&D']
    
    rows = []
    for _ in range(50):
        amount = round(np.random.uniform(50, 6000), 2)
        dept = np.random.choice(depts)
        vendor = np.random.choice(vendors)
        
        status, reason = apply_smart_contracts({'amount': amount, 'department': dept, 'vendor': vendor})
        
        rows.append({
            'transaction_id': f"TXN-{np.random.randint(10000, 99999)}",
            'timestamp': datetime.now() - timedelta(days=np.random.randint(0, 30)),
            'department': dept,
            'vendor': vendor,
            'project': np.random.choice(projects),
            'amount': amount,
            'unit_cost_metric': round(amount / np.random.randint(100, 500), 2), # Cost per User
            'status': status,
            'policy_notes': reason,
            'blockchain_hash': f"0x{np.random.get_state()[1][0]:x}..." # Simulated immutability
        })

    df = pd.DataFrame(rows)
    conn = sqlite3.connect('data_lake.db')
    df.to_sql('transactions', conn, if_exists='append', index=False)
    conn.close()