import pandas as pd
import numpy as np
from datetime import datetime

class PolicyEngine:
    def evaluate(self, amount, dept, vendor):
        # Automated Rule Engine
        if amount > 4000: return "Flagged", "Exceeds $4k Cap"
        if dept == "Sales" and vendor == "AWS": return "Flagged", "Shadow IT"
        return "Approved", "Compliant"

def get_data():
    engine = PolicyEngine()
    depts = ['Engineering', 'Marketing', 'Sales']
    vendors = ['AWS', 'Zoom', 'Slack']
    data = []
    for _ in range(50):
        amt = np.random.uniform(100, 5000)
        d, v = np.random.choice(depts), np.random.choice(vendors)
        status, reason = engine.evaluate(amt, d, v)
        data.append({'timestamp': datetime.now(), 'dept': d, 'vendor': v, 'amount': amt, 'status': status, 'reason': reason})
    return pd.DataFrame(data)