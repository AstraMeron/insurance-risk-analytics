# insurance-risk-analytics
# 🛡️ Insurance Risk Analytics Project: Premium Optimization

### 🎯 Project Goal
The primary objective of this project is to build an advanced, auditable machine learning model to accurately predict motor vehicle **Total Claims**. The goal is to optimize the current premium structure, addressing the portfolio's overall unprofitability identified during the initial analysis.

---

## 🚀 Project Status: Modeling & Pricing Framework Complete (Tasks 1-4)

This repository reflects the completion of the foundational data work, feature engineering, statistical modeling, and the implementation of the core **Risk-Based Premium Optimization Framework**.

## ✅ Key Project Deliverables

### Task 1: Exploratory Data Analysis (EDA) & Stats
The EDA phase confirmed the portfolio's **unprofitability** (Loss Ratio: **104.81%**) and identified critical risk drivers (Geography, Vehicle Type, and Temporal Volatility).
* **Source of Analysis:** See the `EDA.ipynb` notebook.

### Task 2: Data Version Control (DVC)
The project is **reproducible and auditable** by tracking the large raw data file (`data/MachineLearningRating_v3.txt`) using **DVC**.

### Task 3: Feature Engineering & Risk Aggregation
To address high-risk segments, several aggregated risk features were created:
* **Geographic Risk:** A **Zip Code Mean Severity** feature was engineered to quantify the historical claim risk associated with specific geographical areas.
* **Temporal Risk:** Month and Day of Week features were extracted to capture the observed seasonality in claims.

---

### Task 4: Statistical Modeling & Premium Optimization Framework

The core of the project utilizes a **Two-Part Model** approach to calculate the final risk premium.

#### 1. Claim Severity Model (Regression)
* **Goal:** Predict the **amount** of the claim ($\mathbf{S}_{\text{pred}}$), given a claim occurs.
* **Best Model:** **XGBoost Regressor** (RMSE $\approx \$33,011$ on original dollar scale).

#### 2. Claim Frequency Model (Classification)
* **Goal:** Predict the **probability** of a claim occurring ($\mathbf{P}_{\text{claim}}$).
* **Best Model:** **XGBoost Classifier**.

#### 3. Model Interpretability (SHAP Analysis)
SHAP analysis was performed on the best model to ensure auditable feature influence.

| Rank | Feature | Business Implication |
| :--- | :--- | :--- |
| **1** | `SumInsured` | **Highest influence.** Confirms asset value is the primary driver of claim cost. |
| **3** | `log_MeanSeverity` | **Validates geographic risk.** Confirms the engineered Zip Code risk feature is highly predictive. |

#### 4. Risk-Based Premium Formula
The final proposed premium is a function of the model predictions, replacing the current unprofitable pricing method:
$$\text{Premium}_{\text{Risk}} = (\mathbf{P}_{\text{claim}} \times \mathbf{S}_{\text{pred}}) + \text{Expense Loading} + \text{Profit Margin}$$
* The model demonstrated that **current premiums are grossly insufficient**, often failing to even cover the fixed expense loading of the proposed structure.

---

## ⚙️ How to Reproduce the Analysis

To set up this project environment and access the data:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/AstraMeron/insurance-risk-analytics](https://github.com/AstraMeron/insurance-risk-analytics)
    cd insurance-risk-analytics
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install dvc xgboost shap # Added advanced model dependencies
    ```

3.  **Restore the Data (DVC Pull):**
    * **NOTE:** Before pulling, you must configure the DVC remote named `localstorage` using the path where the data was originally stored.
    * After setting up the remote, run:
        ```bash
        dvc pull
        ```
    This command will download the large `MachineLearningRating_v3.txt` file from the DVC cache into your `data/` folder, making the analysis notebooks runnable.