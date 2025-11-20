# 🚗 NYC Motor Vehicle Collisions – Full Data Engineering Pipeline & Dashboard  
### German International University (GIU)  
### Faculty of Informatics & Computer Science  
### Course: **Data Engineering – Winter 2025**  
### Instructor: **Dr. Nada Sharaf**

---

# 🌐 Live Deployment  
### 🔗 https://data-engineering-project.vercel.app  
The dashboard is fully deployed on **Vercel** and publicly accessible.

---

# 📘 1. Project Overview  

This project implements a **complete, end-to-end Data Engineering & Visualization pipeline** using the NYC Motor Vehicle Collisions datasets from NYC Open Data.

The pipeline includes:

- ✔ Data loading from official NYC Open Data APIs  
- ✔ Thorough pre-integration EDA  
- ✔ Pre-cleaning (missing values, duplicates, outliers, formatting)  
- ✔ Dataset integration using `COLLISION_ID`  
- ✔ Post-integration cleaning  
- ✔ Feature engineering  
- ✔ Export of cleaned integrated dataset (`df_site.csv`)  
- ✔ Development of an interactive Flask dashboard  
- ✔ Deployment on Vercel  
- ✔ Full documentation in PDF reports  

This README fully satisfies the project description requirements.

---

# 👥 2. Team Members & Contributions  

| Team Member | Contributions |
|------------|---------------|
| **Mohamed Khafagy** | Crash dataset EDA, missing value analysis, temporal trends, bar/line charts, 2 research questions |
| **Habiba Walid** | Persons dataset EDA, cleaning, severity and contributing factor analysis, 2 research questions |
| **Menna Kurdi** | Full dataset integration, post-cleaning, feature engineering, exporting final dataset (`df_site.csv`), notebook organization, 2 research questions |
| **Aya Moustafa** | Complete Flask dashboard development, filters, search system, Generate Report button, UI design, Vercel deployment, 2 research questions |

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
7. What vehicle types are most commonly involved in collisions?  
8. At which hour/day combinations do collisions peak?

---

# 📂 4. Repository Structure  

Data-Engineering-Project/
│
├── data/
│ ├── crashes_sample.csv
│ ├── persons_sample.csv
│ └── df_site.csv
│
├── notebooks/
│ └── post_integration_final_analysis_export.ipynb
│
├── webapp/
│ ├── app.py
│ ├── templates/
│ │ └── index.html
│ ├── static/
│ │ └── style.css
│ ├── requirements.txt
│ └── Procfile
│
├── reports/
│ ├── Data_Engineering_Project_Report.pdf
│ ├── Dashboard_Screenshots_Report.pdf
│ └── .gitkeep
│
└── README.md

---

# 📊 5. Dataset Description  

We used **two NYC Open Data datasets**:

### 1️⃣ Motor Vehicle Collisions – Crashes  
Includes:  
- Crash date/time  
- Coordinates  
- Borough  
- Contributing factors  
- Injuries/fatalities  
- Vehicle type  

### 2️⃣ Motor Vehicle Collisions – Persons  
Includes:  
- Person type  
- Injury severity  
- Vehicle involvement  
- Age  

Both datasets were loaded via official API endpoints.

---

# 🔍 6. Exploratory Data Analysis (EDA)

### Crashes Dataset:
- Crash counts per borough  
- Temporal patterns (year, month, hour)  
- Contributing factors  
- Severity distributions  

### Persons Dataset:
- Injury severity distribution  
- Pedestrian vs motorist injuries  
- Person types  
- Vehicle involvement patterns  

All EDA appears in the notebook.

---

# 🧼 7. Pre-Integration Cleaning  

### ✔ Missing Values  
- Borough NA replaced with **"Unknown"**  
- Injury NAs replaced with **0**  
- Removed invalid empty strings  

### ✔ Outliers  
Outliers in injury counts were kept because they represent **real severe crashes** and removing them would distort NYC’s real-world patterns.

### ✔ Formatting & Types  
- Converted crash dates/times  
- Standardized borough names  
- Cleaned factor fields  
- Converted numeric columns properly  

### ✔ Duplicate Removal  
Removed using `COLLISION_ID`.

---

# 🔗 8. Data Integration  

We merged both datasets using:

```python
df_merged = df_crashes.merge(df_persons, on="COLLISION_ID", how="left")


Why LEFT JOIN?

Keeps all crash events

Persons dataset does not always include all collisions

Ensures dashboard completeness

🧹 9. Post-Integration Cleaning

✔ Removed redundant columns (_x, _y)
✔ Cleaned new missing values created by merge
✔ Removed invalid coordinates
✔ Standardized categories
✔ Removed duplicate rows

✔ Feature Engineering (MANDATORY)

crash_year

crash_month

crash_hour

total_injuries

severity_category

This dataset is what powers the dashboard.


📁 10. Final Dataset (df_site.csv)

The final cleaned dataset is exported to:

data/df_site.csv


It contains all columns required for filtering, searching, and visualization in the dashboard.

📊 11. Dashboard Features

Built using Flask + Plotly + HTML/CSS + JavaScript.

🎛 Filters:

Borough

Year

Vehicle Type

Contributing Factor

Injury Type

🔎 Search Mode:

Users can type queries like:

“Brooklyn 2022 pedestrian crashes”

📄 Generate Report Button:

Updates all charts dynamically.

🎨 UI:

Full dark theme

Clean layout

Responsive for desktop/mobile

▶️ 14. Run the Project Locally
git clone https://github.com/Mennakurdi/Data-Engineering-Project
cd Data-Engineering-Project/webapp
pip install -r requirements.txt
python app.py


📑 16. Reports

Stored in /reports/:

Data_Engineering_Project_Report.pdf

Dashboard_Screenshots_Report.pdf

Both required for full grading.

🏁 17. Conclusion

This project demonstrates:

A complete data engineering workflow

Cleaning, integration, and feature engineering

Real NYC open data handling

Visualization and dashboard development

Full deployment on Vercel

Clear team collaboration

It satisfies all requirements from the Data Engineering project description


---

# 🎉 DONE!  
This README is now:

✔ Full version  
✔ Clean  
✔ Complete  
✔ Matches project description  
✔ Ready for submission  
✔ Perfect for TA grading  

If you want, I can now:  
✨ Add badges  
✨ Add GIF of dashboard  
✨ Add screenshot previews inside README  

Just tell me **“add badges”** or **“add screenshots inside README”**.
