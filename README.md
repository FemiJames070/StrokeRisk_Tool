# StrokeRisk Tool

**Project Phase 5: Cloud Deployment**  
**Course:** Web Development and Cloud Computing – ARTI404  
**Group 4 (G4 Pulse):** Fuad, Preston, Marrium, and Femi James  

**Live App:** [StrokeRisk Tool](https://strokerisktool.streamlit.app/)  
**GitHub Repository:** [StrokeRisk_Tool](https://github.com/FemiJames070/StrokeRisk_Tool.git)

---

## 📌 Introduction

Stroke is one of the leading causes of death and long-term disability worldwide. Early detection of high-risk individuals can improve outcomes, reduce healthcare costs, and save lives.  

The **StrokeRisk Application** uses **machine learning** to predict stroke risk from demographic, lifestyle, and medical data. Built with the **CRISP-DM** methodology and grounded in **responsible AI principles**, the application features:

- **Accurate Predictions** – Ensemble of top-performing ML models.
- **What-if Analysis** – Explore preventive scenarios.
- **Interpretability** – SHAP-based feature explanations.
- **Ethical & Human-Centered Design** – Fairness monitoring, transparency, and usability focus.

---

## 1️⃣ Business Understanding

**Problem Statement:**  
Develop a scalable, data-driven clinical decision support tool to help healthcare professionals identify high-risk patients before stroke onset.

**Scope:**  
Predict stroke risk using patient demographic and medical data.

**Value Proposition:**  
Identify 80% of high-risk patients earlier than current methods, potentially reducing stroke-related readmissions by 15%.

**Stakeholders:**
| Stakeholder           | Role                 | Interest                                |
|-----------------------|----------------------|------------------------------------------|
| Healthcare Providers  | Frontline users      | Early detection, patient prioritization |
| Hospital Admins       | Oversight            | Reduce readmissions, cut costs          |
| Data Science Team     | Model builders       | Maintain accuracy and reliability       |
| IT Team               | Deployment           | Secure, scalable integration            |
| Patients              | End beneficiaries    | Preventative care access                |
| Public Health Agencies| Population health    | Scale prevention programs               |
| Insurance Providers   | Risk managers        | Lower claims via early intervention     |

**Business Goals:**
- Detect ≥80% of high-risk patients early.
- Reduce stroke-related readmissions by 15%.
- Improve care efficiency with patient prioritization.
- Enable data-driven prevention strategies.
- Build a scalable AI framework for broader health risk prediction.

---

## 2️⃣ Data Understanding

**Source:** Public stroke dataset (`stroke.csv`) with demographic, lifestyle, and medical history.

**Key Features:** Age, hypertension, heart disease, BMI, smoking status, glucose levels, work type, marital status, residence type.  
**Target Variable:** `stroke` (binary: 1 = Yes, 0 = No).  

**Challenges:**
- Class imbalance (~5% stroke cases).
- Missing BMI values.
- No temporal/geographic data.

**Findings:**
- Strong correlation: Age, hypertension, glucose levels.
- Moderate: Smoking status, marital status.
- Weak but relevant: Work type, residence type.

---

## 3️⃣ Data Preparation

- **Missing Values:** Median imputation by age group for BMI.
- **Encoding:** One-hot encoding (`drop_first=True`).
- **Scaling:** `StandardScaler` after SMOTE.
- **Class Imbalance:** SMOTE to 50:50 ratio.
- **Split:** 80/20 train-test with stratification.
- **Ethics:** Retained ambiguous entries, logged preprocessing steps.

---

## 4️⃣ Modeling & Evaluation

**Models Tested:**
- Random Forest (Best overall accuracy ~0.96)
- XGBoost (Strong accuracy, unique feature insights)
- Extra Trees (Lowest false positives, balanced F1)
- LightGBM (Competitive but less stable)
- Decision Tree (Baseline, overfit)

**Evaluation Metrics:** Accuracy, Recall, Precision, F1-score, AUC-ROC, Confusion Matrix, Feature Importance.

**Deployment Choice:**  
Three-model ensemble (**Random Forest + XGBoost + Extra Trees**) plus a combined meta-model.  
Hyperparameter tuning showed no significant improvement.

---

## 5️⃣ Front-End & Human-Centered Design

Built with **Streamlit** using **Human-Centered Design** and the **Fogg Behavior Model (B=MAT)**.

**Key Principles:**
- **Motivation:** Clinical impact, trust, transparency (SHAP visualizations).
- **Ability:** Low friction (≤2 clicks), accessibility (WCAG-compliant).
- **Trigger:** Integration into patient intake and screenings.

**Main UI Pages:**
- **Landing Page** – Quick access CTAs.
- **Patient Data Entry** – Guided form.
- **Risk Assessment** – Probability, category, contributing factors.
- **Records Management** – CRUD operations.
- **Practitioner & Patient Profiles** – Overview of key data.
- **Model Performance** – Metrics & fairness indicators.
- **System Settings** – Thresholds, preferences.
- **Data Privacy & Consent** – Notification & consent controls.
- **Help & Support**, **Contact Us**, **About Us**.

---

## 6️⃣ Deployment

**Version Control:** Git + GitHub.  
**Hosting:** Streamlit Cloud.  
**Database:** SQLite (future: scalable DB).  
**Security:** Encryption (GDPR, PHIPA, HIPAA compliance), role-based access.

**Backend Models:** Ensemble model with option to view individual model predictions.

**Monitoring & Feedback:**
- **Performance Drift:** EvidentlyAI.
- **Fairness Audits:** Scheduled subgroup checks.
- **Feedback Loop:** Clinician validation forms.

---

## 7️⃣ Potential Harms & Mitigation

| Harm                    | Real-World Case      | Mitigation                          |
|-------------------------|----------------------|--------------------------------------|
| Discriminatory Predictions | Optum Cost Algorithm | Subgroup audits, fairness-aware models |
| Automation Bias         | AI Imaging Tools     | Human-in-the-loop                    |
| Exclusion of Vulnerable Data | Sepsis Model Failures | Inclusive preprocessing              |
| Transparency Deficit    | General AI Critiques | Consent banners, model cards         |

---

## 8️⃣ Conclusion & Next Steps

The StrokeRisk application delivers **real-time, explainable stroke risk predictions** using an ensemble ML backend and ethical design practices.

**Next Steps:**
- Integrate secure multi-clinic database.
- Pilot with healthcare providers.
- Expand predictive scope to cardiovascular conditions.

---

## 📂 Additional Documentation

- **Phase 1:** [Business Understanding](https://drive.google.com/file/d/1P7XoourdFPqp3Lw_USbUy06eCNZDEXAN/view?usp=drive_link))
- **Phase 2:** `StrokeRisk_Data Understanding & Preparation.ipynb`
- **Phase 3 & 4:** `StrokeRisk Model Building & Evaluation.ipynb`

---
