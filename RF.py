# ======================= Imports ==========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import MinMaxScaler

# ======================= Data Loading =====================
excel_file = 'data.xlsx'
sheet_name = 'Sheet1'
data_kami2 = pd.read_excel(excel_file, sheet_name=sheet_name)

new_column_names = ['Relative humidity', 'Absorbent weight', 'Temperature', 'Time', r'$SO_2$ concentration']
data_kami2.columns = new_column_names

# ======================= Preprocessing ====================
Xf = data_kami2.iloc[:, 0:4]
yf = data_kami2[[r'$SO_2$ concentration']]

X = Xf.values
Y = yf.values

scaler_X = MinMaxScaler()
X_normalized = scaler_X.fit_transform(X)

scaler_y = MinMaxScaler()
Y_normalized = scaler_y.fit_transform(Y)

# ============== Train / Val / Test Split (70/20/10) ========
X_train_split, X_temp, Y_train_split, Y_temp = train_test_split(
    X_normalized, Y_normalized, test_size=0.3, random_state=20, shuffle=True
)
X_test_split, X_val_split, Y_test_split, Y_val_split = train_test_split(
    X_temp, Y_temp, test_size=2/3, random_state=20, shuffle=True
)

X_train = X_train_split
Y_train = Y_train_split
X_val = X_val_split
Y_val = Y_val_split
X_test = X_test_split
Y_test = Y_test_split

# =============== Model Definition & Training ===============
best_rf = RandomForestRegressor(
    n_estimators=9,
    max_depth=16,
    min_samples_leaf=1,
    criterion='poisson',
    min_samples_split=2,
    n_jobs=-1
)
best_rf.fit(X_train, Y_train.ravel())

# ================== Evaluation ============================
Y_pred_train = best_rf.predict(X_train)
Y_pred_val = best_rf.predict(X_val)

mse_train = mean_squared_error(Y_train.ravel(), Y_pred_train)
rmse_train = np.sqrt(mse_train)
r2_train = r2_score(Y_train.ravel(), Y_pred_train)
mae_train = mean_absolute_error(Y_train.ravel(), Y_pred_train)

mse_val = mean_squared_error(Y_val.ravel(), Y_pred_val)
rmse_val = np.sqrt(mse_val)
r2_val = r2_score(Y_val.ravel(), Y_pred_val)
mae_val = mean_absolute_error(Y_val.ravel(), Y_pred_val)

print("Evaluation Metrics for the Best Model:")
print(f"Training set: MSE = {mse_train:.4f}, RMSE = {rmse_train:.4f}, R2 = {r2_train:.4f}, MAE = {mae_train:.4f}")
print(f"Validation set: MSE = {mse_val:.4f}, RMSE = {rmse_val:.4f}, R2 = {r2_val:.4f}, MAE = {mae_val:.4f}")

# ================= Learning Curve ==========================
train_sizes, train_scores, val_scores = learning_curve(
    estimator=best_rf,
    X=X_train,
    y=Y_train.ravel(),
    cv=5,
    scoring='neg_root_mean_squared_error',
    train_sizes=np.linspace(0.1, 1.0, 10),
    n_jobs=-1
)

train_rmse = -np.mean(train_scores, axis=1)
val_rmse = -np.mean(val_scores, axis=1)

plt.figure(figsize=(8, 6))
plt.plot(train_sizes, train_rmse, 'o-', label='Training RMSE')
plt.plot(train_sizes, val_rmse, 'o-', label='Validation RMSE')
plt.xlabel('Training Set Size')
plt.ylabel('RMSE')
plt.title('Learning Curve (Random Forest)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
