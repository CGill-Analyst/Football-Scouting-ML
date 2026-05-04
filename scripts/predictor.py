import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import os
from datetime import datetime

# ==========================================
# ⚙️ SETTINGS
# ==========================================
# Ensure your football_data.csv is inside the 'data' folder!
FILE_PATH = r'C:\Users\charl\PycharmProjects\PythonProject\Automations\data\football_data.csv'
MAX_AGE = 23


def run_scouting_engine():
    try:
        # 1. Load Data
        df = pd.read_csv(FILE_PATH, sep=None, engine='python', on_bad_lines='skip')

        # 2. Mapping & Cleaning
        mapping = {'Gls': 'Goals', 'Ast': 'Assists', 'Min': 'Minutes_Played', 'Int': 'Interceptions',
                   'SoT%': 'Pass_Accuracy'}
        df = df.rename(columns=mapping)
        df = df[df['Player'] != 'Player']

        cols_to_fix = ['Goals', 'Assists', 'Interceptions', 'Minutes_Played', 'Pass_Accuracy', 'Age']
        for col in cols_to_fix:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

        # 3. Apply Filters
        df = df[df['Age'] <= MAX_AGE].copy()
        df = df[df['Minutes_Played'] >= 90].copy()

        # 4. Feature Engineering
        for metric in ['Goals', 'Assists', 'Interceptions']:
            df[f'{metric}_per_90'] = (df[metric] / df['Minutes_Played']) * 90

        df['Performance_Score'] = (df['Goals_per_90'] * 0.4) + (df['Assists_per_90'] * 0.3) + (
                    df['Interceptions_per_90'] * 0.3)

        # 5. ML Model
        X = df[['Pass_Accuracy', 'Interceptions_per_90']]
        y = df['Performance_Score']
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        df['Predicted_Score'] = model.predict(X)

        # 6. Rank Results
        df['Value_Difference'] = df['Performance_Score'] - df['Predicted_Score']
        results = df.sort_values(by='Value_Difference', ascending=False)

        # ==========================================
        # 📂 THE NEW SAVE LOGIC (Replaces old .to_csv)
        # ==========================================
        # Create reports folder if missing
        if not os.path.exists('reports'):
            os.makedirs('reports')

        # Generate unique name: Scouting_Report_U23_20260504_2105.csv
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        output_name = f"Scouting_Report_U{MAX_AGE}_{timestamp}.csv"
        # Use ".." to save it in the reports folder which is outside the scripts folder
        output_path = os.path.join("..", "reports", output_name)

        results.to_csv(output_path, index=False)

        print(f"\n✅ ANALYSIS COMPLETE")
        print(f"Top Gem Found: {results['Player'].iloc[0]} ({results['Squad'].iloc[0]})")
        print(f"Saved to: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    run_scouting_engine()