import pandas as pd
import numpy as np
import datetime
import sqlite3

def generate_mock_data():
    departments = ['Marketing', 'Engineering', 'Sales', 'HR', 'Operations']
    projects = ['Project Alpha', 'Project Beta', 'Cloud Migration', 'Recruitment Drive']
    vendors = ['AWS', 'Zoom', 'Delta Airlines', 'Apple', 'Slack']
    
    data = []
    for i in range(100):
        dept = np.random.choice(departments)
        vendor = np.random.choice(vendors)
        amount = round(np.random.uniform(10, 5000), 2)
        
        # Policy Engine (The "Smart Contract" Logic)
        status = "Approved"
        reason = "Within Budget"
        if amount > 4000:
            status = "Flagged"
            reason = "Exceeds $4k Cap"
        elif dept == 'Sales' and vendor == 'AWS':
            status = "Flagged"
            reason = "Shadow IT: Unauthorized Vendor"

        data.append({
            'timestamp': datetime.datetime.now() - datetime.timedelta(days=np.random.randint(0, 30)),
            'department': dept,
            'project': np.random.choice(projects),
            'vendor': vendor,
            'amount': amount,
            'status': status,
            'reason': reason,
            'owner': f"User_{np.random.randint(1, 10)}"
        })
    
    conn = sqlite3.connect('finops_datalake.db')
    pd.DataFrame(data).to_sql('expenditures', conn, if_exists='replace', index=False)
    conn.close()
    print("✅ Data Lake Updated!")

if __name__ == "__main__":
    generate_mock_data()