# StrokeRisk AI System

**Project Phase:** 5 (Full Lifecycle: Development $\rightarrow$ MLOps $\rightarrow$ Deployment)  
**Course:** AI Development, Web Development and Cloud Computing 
**Lead Architect:** Oluwafemi (Femi) James

**Contributing Teams:**
* **Phase 1 (Development):** Group 4 (G4 Pulse) – *Fuad, Preston, Marrium, Femi*
* **Phase 2 (Maintenance & MLOps):** Group 2 – *Kevin, Shalin, Femi*

**Live App:** [StrokeRisk Tool](https://strokerisktool.streamlit.app/Patient_Data_Entry)  
**GitHub Repository:** [StrokeRisk_Tool](https://github.com/FemiJames070/StrokeRisk_Tool.git)

---

## 📌 Introduction

Stroke is one of the leading causes of death and long-term disability worldwide. Early detection of high-risk individuals can improve outcomes, reduce healthcare costs, and save lives.

The **StrokeRisk Application** is not just a predictive tool; it is a **governed AI system**. It uses machine learning to predict stroke risk from demographic and medical data, built on the **CRISP-DM** methodology. Uniquely, it integrates a "Governance-as-Code" layer using **MLflow** to ensure that every prediction is traceable, reproducible, and compliant with healthcare standards (FDA SaMD/PIPEDA).

### Key Capabilities:
- **Accurate Predictions** – Soft-Voting Ensemble of top-performing ML models.
- **Governance-as-Code** – Immutable audit trails and reproducibility locks.
- **Interpretability** – SHAP-based feature explanations for clinician trust.
- **Ethical Design** – Fairness monitoring and Human-Centered UI.

---

## 1️⃣ Business Understanding

**Problem Statement:** Healthcare providers lack an efficient, proactive, and *auditable* way to identify individuals at high risk of stroke.

**Value Proposition:** Identify 80% of high-risk patients earlier than current methods, reducing stroke-related readmissions by 15%, while maintaining strict regulatory compliance through MLOps.

**Stakeholders:**
| Stakeholder | Role | Interest |
| :--- | :--- | :--- |
| **Healthcare Providers** | Frontline users | Early detection, patient prioritization |
| **Data Science Team** | Model Governance | Accuracy, bias auditing, and version control |
| **Patients** | End beneficiaries | Preventative care access & data privacy |
| **Auditors/Regulators** | Compliance | Traceability of model decisions (PIPEDA/FDA) |

---

## 2️⃣ Data Understanding & Preparation

**Source:** Public stroke dataset (`stroke.csv`) with 5,110 patient records.  
**Target Variable:** `stroke` (Binary Classification).

**Key Challenges & Solutions:**
* **Class Imbalance:** Only ~5% stroke cases. Solved using **SMOTE** (Synthetic Minority Over-sampling Technique) to achieve a 50:50 training split.
* **Missing Data:** Median imputation grouped by `Age` and `Gender` for BMI.
* **Data Integrity:** Implemented `log_input(dataset)` in MLflow to create a digest of the training data for every run.

---

## 3️⃣ Phase 1: Modeling & The Ensemble Innovation

To solve the "Accuracy Paradox" (where a model predicts "No Stroke" 95% of the time and claims high accuracy), we moved beyond single models.

**Models Evaluated:**
* Random Forest (Baseline)
* XGBoost (High Variance)
* Extra Trees (Low Bias)

**The Innovation:**
We developed a **Soft-Voting Ensemble Model (v4.0)** that aggregates the probability outputs of all three base models.
* **Result:** Stabilized variance and maximized **Recall (96.5%)**, ensuring the system minimizes false negatives (missed diagnoses).

---

## 4️⃣ Phase 2: MLOps & Governance-as-Code



This phase transformed the project from a "research notebook" into a "production system." We implemented an immutable audit trail using **MLflow** to satisfy **PIPEDA & FDA SaMD** reproducibility guidelines.

**Core Governance Features:**

* **Reproducibility:** Enforced `conda.yaml` environment locking. This prevents "dependency drift," ensuring the model runs exactly the same way in Production as it did in Development.
* **Auditability:** Every single training run logged:
    * **Git Commit Hash:** Links the model binary to the exact code version.
    * **Dataset Digest:** Proves exactly which patient data was used.
    * **Parameters:** Hyperparameters for Random Forest/XGBoost.
* **Gated Promotion:** Implemented a strict **Staging $\rightarrow$ Production** workflow. Models cannot be deployed without passing specific validation thresholds (Recall > 95%) and receiving manual approval in the Model Registry.

| Component | Tool Used | Purpose |
| :--- | :--- | :--- |
| **Tracking Server** | MLflow | Centralized log of metrics and artifacts. |
| **Model Registry** | MLflow | Version control for AI models (v1.0 $\rightarrow$ v4.0). |
| **Environment** | Conda | Dependency isolation. |

---

## 5️⃣ Phase 5: Front-End & Deployment

**Architecture:** The system is deployed on **Streamlit Cloud**, serving the MLflow-registered model via a backend API.

**Human-Centered Design (B=MAT):**
* **Motivation:** We build trust by visualizing *why* the AI made a decision using **SHAP** plots (e.g., "High Glucose increased risk by 15%").
* **Ability:** The "Patient Data Entry" form is optimized for clinical workflows (under 30 seconds to complete).

**Main UI Pages:**
* **Patient Data Entry:** Guided input form.
* **Risk Assessment:** Real-time probability scoring.
* **Practitioner Profile:** Overview of patient population statistics.
* **System Settings:** Sensitivity thresholds configuration.

---

## 6️⃣ Potential Harms & Mitigation

| Harm | Mitigation Strategy |
| :--- | :--- |
| **Discriminatory Predictions** | **Subgroup Audits:** We monitor Recall rates across Gender and Age groups to detect bias. |
| **Automation Bias** | **Human-in-the-Loop:** The UI explicitly states this is a "Decision Support Tool," not a diagnosis. |
| **Model Drift** | **Retraining Protocol:** Weekly monitoring of data distribution (PSI/KS Test). |

---

## 📂 Documentation

### 🔬 Part 1: AI Development (G4 Pulse)
*Focus: Data Science, Modeling, and Clinical Validation*
- **Phase 1:** [Business Understanding & Objectives](https://drive.google.com/file/d/1P7XoourdFPqp3Lw_USbUy06eCNZDEXAN/view?usp=drive_link)
- **Phase 2:** [Data Preparation & EDA Report](https://drive.google.com/file/d/1MtRAzNDO4Ty9QOEIlTLsTaXKlE60Vj0g/view?usp=drive_link)
- **Phase 3 & 4:** [Model Creation, Training & Evaluation](https://drive.google.com/file/d/1fckHXpVdK5yX1S1W8FHYW6YgbyuJoWw7/view?usp=drive_link)

### 🛡️ Part 2: MLOps & Governance (Group 2)
*Focus: System Design, Lifecycle Management, and Compliance*
- **Phase 1:** [Maintenance System Design & Planning](https://drive.google.com/file/d/1KFP1qpmSbCbi7MpDgqD3sk1ellMhR1Yt/view?usp=drive_link)
- **Phase 2:** [MLOps Development & Implementation](https://drive.google.com/file/d/1uZFo58xYIr5LmNQUQlEvyQ1HrUC5ntoA/view?usp=drive_link)
- **Phase 3:** [System Reflection & Finalization](https://drive.google.com/file/d/1pTO8-F4HyFeZzWXjbv_Vmfxj6Ea_PTMB/view?usp=drive_link)
- **Full Suite:** [Complete Documentation Suite](https://drive.google.com/file/d/1-EIn7YQ-TX6cVogcKJyA1uZK-1oYI8JA/view?usp=drive_link)
