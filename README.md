# insurance-risk-analytics
# 🛡️ Insurance Risk Analytics Project: Premium Optimization

### 🎯 Project Goal
The primary objective of this project is to build an advanced, auditable machine learning model to accurately predict motor vehicle **Total Claims**. The goal is to optimize the current premium structure, addressing the portfolio's overall unprofitability identified during the initial analysis.

---

## 📅 Interim Submission Status (Tasks 1 & 2 Complete)

This repository reflects the completion of the foundational Data Quality Assessment (Task 1) and the setup of the auditable data infrastructure (Task 2).

### ✅ Task 1: Exploratory Data Analysis (EDA) & Stats

The EDA phase focused on data cleaning, statistical analysis, and identifying risk patterns.

**Key Findings:**

* **Unprofitability:** The overall portfolio Loss Ratio (Total Claims / Total Premium) is **104.81%**, confirming the need for urgent premium optimization.
* **Target Distribution:** The target variable (`TotalClaims`) is highly **zero-inflated** (Median: 0.00) and extremely skewed, requiring specialized modeling techniques (e.g., a two-part model).
* **High-Risk Segments:**
    * **Geography:** **Gauteng** and specific **Postal Codes** show significantly higher average claims than the portfolio average.
    * **Vehicle Type:** **Heavy Commercial** vehicles are the highest-risk segment (Loss Ratio > 160%).
* **Temporal Trend:** Claims show significant **seasonality/volatility** (e.g., spikes in December), which will be incorporated into feature engineering.

**Source of Analysis:** See the `EDA.ipynb` notebook for full code, statistics, and visualizations.

### ✅ Task 2: Data Version Control (DVC)

To ensure the project is fully **reproducible and auditable**, the large raw data file has been versioned using DVC.

* **Version Control:** The large raw data file (`data/MachineLearningRating_v3.txt`) is no longer tracked by Git. Instead, DVC tracks its version, allowing us to revert to any state of the data used for training.
* **Setup:** DVC is initialized, and a local remote storage (`localstorage`) is configured to hold the data content.

---

## ⚙️ How to Reproduce the Analysis

To set up this project environment and access the data:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/AstraMeron/insurance-risk-analytics
    cd insurance-risk-analytics
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    pip install dvc # DVC is a separate install
    ```

3.  **Restore the Data (DVC Pull):**
    * **NOTE:** Before pulling, you must configure the DVC remote named `localstorage` using the path where the data was originally stored.
    * After setting up the remote, run:
        ```bash
        dvc pull
        ```
    This command will download the large `MachineLearningRating_v3.txt` file from the DVC cache into your `data/` folder, making the `EDA.ipynb` file runnable.