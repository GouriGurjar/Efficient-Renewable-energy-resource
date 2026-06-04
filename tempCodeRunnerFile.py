"""
╔══════════════════════════════════════════════════════════════════╗
║  RUN THIS ONCE — Re-saves model files with current sklearn       ║
║  Run from your project root:  python retrain_and_save.py         ║
║  Then upload the 3 files from models/ folder to GitHub root.     ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os, pickle, joblib, numpy as np, pandas as pd
from pathlib import Path
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error

# ── Paths ──────────────────────────────────────────────────────────
DATA_PATH  = "data/renewable_energy_data.csv"   # adjust if needed
OUT_DIR    = "models"
Path(OUT_DIR).mkdir(exist_ok=True)

# ── Feature / target columns (must match app.py exactly) ──────────
FEATURE_COLS = [
    "Hour", "Day", "Month", "Day_of_Week", "Day_of_Year", "Season",
    "Temperature", "Solar_Irradiance", "Wind_Speed", "Humidity",
    "Precipitation", "Pressure",
    "Hour_sin", "Hour_cos", "Month_sin", "Month_cos", "DoY_sin", "DoY_cos",
    "Wind_cubed", "Irr_temp_eff", "Humidity_precip",
]
TARGET_COLS = [
    "Solar_Energy", "Wind_Energy", "Hydro_Energy",
    "Biomass_Energy", "Geothermal_Energy",
]

# ── Load data ──────────────────────────────────────────────────────
print(f"📂 Loading dataset from {DATA_PATH} ...")
df = pd.read_csv(DATA_PATH, parse_dates=["Datetime"])
print(f"   {len(df):,} rows loaded")

# ── Recreate engineered features if missing ────────────────────────
if "Hour_sin" not in df.columns:
    df["Hour_sin"]        = np.sin(2 * np.pi * df["Hour"] / 24)
    df["Hour_cos"]        = np.cos(2 * np.pi * df["Hour"] / 24)
    df["Month_sin"]       = np.sin(2 * np.pi * df["Month"] / 12)
    df["Month_cos"]       = np.cos(2 * np.pi * df["Month"] / 12)
    df["DoY_sin"]         = np.sin(2 * np.pi * df["Day_of_Year"] / 365)
    df["DoY_cos"]         = np.cos(2 * np.pi * df["Day_of_Year"] / 365)
    df["Wind_cubed"]      = df["Wind_Speed"] ** 3
    df["Irr_temp_eff"]    = df["Solar_Irradiance"] * (1 - 0.004 * np.maximum(0, df["Temperature"] - 25))
    df["Humidity_precip"] = df["Humidity"] * df["Precipitation"]

# ── Train / test split (80/20 time-based) ─────────────────────────
split    = int(len(df) * 0.8)
train_df = df.iloc[:split]
test_df  = df.iloc[split:]

X_train  = train_df[FEATURE_COLS]
y_train  = train_df[TARGET_COLS]
X_test   = test_df[FEATURE_COLS]
y_test   = test_df[TARGET_COLS]

# ── Scale ──────────────────────────────────────────────────────────
print("⚙️  Fitting StandardScaler ...")
scaler      = StandardScaler()
X_train_sc  = scaler.fit_transform(X_train)
X_test_sc   = scaler.transform(X_test)

# ── Train Total_Energy GBR (this is model.joblib used by app.py) ──
print("🤖 Training GradientBoostingRegressor for Total_Energy ...")
total_model = GradientBoostingRegressor(
    n_estimators=200, max_depth=5, learning_rate=0.08,
    subsample=0.8, random_state=42
)
total_model.fit(X_train_sc, train_df["Total_Energy"])

total_pred = total_model.predict(X_test_sc)
print(f"   R²  = {r2_score(test_df['Total_Energy'], total_pred):.4f}")
print(f"   MAE = {mean_absolute_error(test_df['Total_Energy'], total_pred):.2f} kWh")

# ── Train multi-output model (multi_model.joblib) ─────────────────
print("🤖 Training MultiOutputRegressor for 5 sources ...")
multi_model = MultiOutputRegressor(
    GradientBoostingRegressor(
        n_estimators=200, max_depth=5, learning_rate=0.08,
        subsample=0.8, random_state=42
    ),
    n_jobs=-1
)
multi_model.fit(X_train_sc, y_train)

# ── Save ───────────────────────────────────────────────────────────
print("💾 Saving model files ...")
joblib.dump(total_model, os.path.join(OUT_DIR, "model.joblib"))
joblib.dump(scaler,      os.path.join(OUT_DIR, "scaler.joblib"))
with open(os.path.join(OUT_DIR, "model_features.pkl"), "wb") as f:
    pickle.dump(FEATURE_COLS, f)
joblib.dump(multi_model, os.path.join(OUT_DIR, "multi_model.joblib"))

print()
print("✅ Done! Files saved:")
print(f"   models/model.joblib")
print(f"   models/scaler.joblib")
print(f"   models/model_features.pkl")
print(f"   models/multi_model.joblib")
print()
print("📤 Next steps:")
print("   1. Upload these 3 files to your GitHub repo ROOT:")
print("      model.joblib  |  scaler.joblib  |  model_features.pkl")
print("   2. Reboot your Streamlit app")
print("   3. Yellow warning will be gone ✅")