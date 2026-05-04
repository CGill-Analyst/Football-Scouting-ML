# ⚽️ U23 Scouting Engine: Predictive Talent Identification

An automated machine learning tool designed to identify undervalued football prospects across European leagues. This project uses a **Random Forest Regressor** to find players who are statistically overperforming relative to their expected technical output.

## 🚀 Key Features
*   **Automated Reporting:** Generates timestamped CSV scouting reports.
*   **ML Integration:** Uses Scikit-Learn to establish performance baselines.
*   **Smart Filtering:** Focuses on U23 players with significant minutes played.

## 📁 Project Structure
*   **/scripts**: Core Python logic (`predictor.py`).
*   **/data**: Raw player data (excluded from repo for size/privacy).
*   **/reports**: Automated scouting outputs.

## 🛠 Tech Stack
*   **Python** (Pandas, Scikit-Learn, NumPy)

## 📊 Top Scouting Discoveries (May 2026)
Below are the top 5 "Hidden Gems" identified by the engine in the most recent run. These players show the highest positive deviation from their predicted performance baselines.

| Player | Squad | Age | Value Difference |
| :--- | :--- | :--- | :--- |
| **Stanis Idumbo** | Monaco | 20 | **+0.292** |
| **Dilane Bakwa** | Strasbourg | 23 | **+0.251** |
| **Stefanos Tzimas** | Brighton | 20 | **+0.249** |

> *Note: A higher Value Difference indicates the player is significantly overperforming their expected technical output based on current age and league difficulty.*
