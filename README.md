# 🚗 NYC Motor Vehicle Collisions – Full Data Engineering Pipeline & Dashboard  
### German International University (GIU)  
### Faculty of Informatics & Computer Science  
### Course: **Data Engineering – Winter 2025**  
### Instructor: **Dr. Nada Sharaf**

---

# 🌐 Live Deployment  
### 🔗 https://data-engineering-project.vercel.app  
The dashboard is fully deployed on **Vercel** and accessible publicly.

---

# 📘 1. Project Overview  

This project implements an **end-to-end Data Engineering and Visualization pipeline** using the NYC Motor Vehicle Collisions datasets from NYC Open Data.  
It includes:

- ✔ Dataset loading  
- ✔ Pre-integration EDA  
- ✔ Pre-cleaning (missing values, duplicates, outliers)  
- ✔ Dataset integration using `COLLISION_ID`  
- ✔ Post-integration cleaning  
- ✔ Feature engineering  
- ✔ Final cleaned dataset generation  
- ✔ Interactive dashboard using Flask + Plotly  
- ✔ Deployment on Vercel  
- ✔ Final PDF reports  

This README follows all instructions required in the official project description.

---

# 👥 2. Team Members & Contributions  

| Team Member | Contributions |
|------------|---------------|
| **Mohamed Khafagy** | EDA on crashes dataset, missing value analysis, temporal trends, bar/line charts, 2 research questions |
| **Habiba Walid** | EDA on persons dataset, cleaning, severity analysis, contributing factor analysis, 2 research questions |
| **Menna Kurdi** | Full integration of datasets, post-cleaning, feature engineering, creation of final dataset (`df_site.csv`), notebook organization, 2 research questions |
| **Aya Moustafa** | Full Flask dashboard implementation, UI/UX design, filters, search feature, Generate Report button, deployment on Vercel, 2 research questions |

---

# 🎯 3. Research Questions (8 Total)  

### Mohamed  
1. Which borough experiences the highest number of collisions yearly?  
2. How do total crashes trend across the years?

### Habiba  
3. What are the top contributing factors that lead to severe injuries?  
4. Which weekdays record the highest injury counts?

### Menna  
5. How do pedestrian vs. motorist injuries compare across NYC?  
6. How did crash severity (injured vs. killed) evolve over the years?

### Aya  
7. Which vehicle types are most commonly involved in collisions?  
8. At which hour/day combinations do collisions peak?

---

# 📂 4. Repository Structure  



---

# 📊 5. Dataset Description  

We used **two NYC Open Data datasets**:

### 1️⃣ Motor Vehicle Collisions – Crashes  
Includes:  
- Crash date & time  
- Coordinates  
- Borough  
- Vehicle info  
- Contributing factors  
- Injuries & fatalities  

### 2️⃣ Motor Vehicle Collisions – Persons  
Includes:  
- Person type  
- Injury severity  
- Vehicle association  

Both datasets were loaded using the official API endpoints.

---

# 🔍 6. Exploratory Data Analysis (EDA)

Performed separately on both datasets:

### Crashes Dataset EDA
- Frequency analysis  
- Borough distribution  
- Time-based patterns (year, month, hour)  
- Contributing factors  
- Severity levels  

### Persons Dataset EDA
- Injury categories  
- Affected groups (drivers, passengers, pedestrians)  
- Severity distribution  
- Age distribution  

---

# 🧼 7. Pre-Integration Cleaning  

✔ Handled missing values  
✔ Fixed data types  
✔ Standardized borough names  
✔ Removed duplicates using `COLLISION_ID`  
✔ Outlier analysis (injury counts)  
✔ Cleaned empty strings / invalid values  

All cleaning was done **before merging**.

---

# 🔗 8. Data Integration  

We merged crashes + persons using:

```python
df_merged = df_crashes.merge(df_persons, on="COLLISION_ID", how="left")
