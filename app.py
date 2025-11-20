from flask import Flask, render_template, request
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

# ============================================
# Load df_site.csv
# ============================================
DATA_PATH = os.path.join(os.path.dirname(__file__), "df_site.csv")
df = pd.read_csv(DATA_PATH)

# Convert dates
df["crash_date"] = pd.to_datetime(df["crash_date"], errors="coerce")
df["crash_day"] = df["crash_date"].dt.day_name()
df["crash_hour"] = pd.to_datetime(df["crash_time"], errors="coerce").dt.hour
df["crash_month"] = df["crash_date"].dt.to_period("M").astype(str)

# ============================================
# Dropdowns
# ============================================
BOROUGHS = sorted(df["borough"].dropna().unique())
YEARS = sorted(df["crash_year"].dropna().unique())
VEH_TYPES = sorted(df["vehicle_type_code1"].dropna().unique())
FACTORS = sorted(df["contributing_factor_vehicle_1"].dropna().unique())
INJURY_TYPES = ["Total", "Pedestrian", "Cyclist", "Motorist"]

# ============================================
# Styling for charts
# ============================================
def style_fig(fig, height=400):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0e0e0e",
        plot_bgcolor="#0e0e0e",
        font=dict(color="white", size=12),
        margin=dict(l=40, r=40, t=60, b=40),
        height=height
    )
    return fig

# ============================================
# Filtering Function
# ============================================
def filter_data(boro, year, vehicle, factor, injury):
    filtered = df.copy()

    if boro != "All":
        filtered = filtered[filtered["borough"] == boro]

    if year != "All":
        filtered = filtered[filtered["crash_year"] == int(year)]

    if vehicle != "All":
        filtered = filtered[filtered["vehicle_type_code1"] == vehicle]

    if factor != "All":
        filtered = filtered[filtered["contributing_factor_vehicle_1"] == factor]

    if injury == "Pedestrian":
        filtered = filtered[filtered["number_of_pedestrians_injured"] > 0]

    elif injury == "Cyclist":
        filtered = filtered[filtered["number_of_cyclist_injured"] > 0]

    elif injury == "Motorist":
        filtered = filtered[filtered["number_of_motorist_injured"] > 0]

    return filtered

# ============================================
# Smart Search Parser
# ============================================
def parse_search(text):
    text = text.lower().strip()
    if text == "":
        return "All", "All", "All", "All", "Total"

    boro = "All"
    year = "All"
    vehicle = "All"
    factor = "All"
    injury = "Total"

    for b in BOROUGHS:
        if b.lower() in text:
            boro = b

    for w in text.split():
        if w.isdigit() and len(w) == 4:
            year = w

    if "pedestrian" in text or "ped" in text:
        injury = "Pedestrian"
    elif "cyclist" in text or "bike" in text:
        injury = "Cyclist"
    elif "motorist" in text or "driver" in text:
        injury = "Motorist"

    return boro, year, vehicle, factor, injury


# ============================================
# Render Dashboard
# ============================================
@app.route("/", methods=["GET", "POST"])
def home():

    boro = request.form.get("borough", "All")
    year = request.form.get("year", "All")
    veh = request.form.get("vehicle", "All")
    factor = request.form.get("factor", "All")
    injury = request.form.get("injury", "Total")
    search_text = request.form.get("search", "")

    # Search overrides dropdown filters
    if search_text.strip() != "":
        boro, year, veh, factor, injury = parse_search(search_text)

    filtered = filter_data(boro, year, veh, factor, injury)

    # ===============================
    # 1. Bar: Crashes per Borough
    # ===============================
    borough_counts = filtered["borough"].fillna("UNKNOWN").value_counts().reset_index()
    borough_counts.columns = ["borough", "crash_count"]
    fig1 = style_fig(
        px.bar(borough_counts, x="borough", y="crash_count", title="Crashes per Borough")
    )

    # ===============================
    # 2. Monthly Trend
    # ===============================
    monthly = filtered.groupby("crash_month").size().reset_index(name="crash_count")
    fig2 = style_fig(
        px.line(monthly, x="crash_month", y="crash_count", title="Monthly Crash Trend", markers=True)
    )

    # ===============================
    # 3. Top Contributing Factors
    # ===============================
    factor_counts = (
        filtered["contributing_factor_vehicle_1"]
        .fillna("UNKNOWN")
        .value_counts()
        .head(10)
        .reset_index()
    )
    factor_counts.columns = ["factor", "crash_count"]
    fig3 = style_fig(
        px.bar(factor_counts, x="crash_count", y="factor", orientation="h",
               title="Top 10 Contributing Factors")
    )

    # ===============================
    # 4. Heatmap: Day vs Hour
    # ===============================
    if "crash_day" in filtered.columns and "crash_hour" in filtered.columns:
        heat = filtered.pivot_table(index="crash_day", columns="crash_hour",
                                    aggfunc="size", fill_value=0)
        fig4 = px.imshow(
            heat,
            labels=dict(x="Hour of Day", y="Day", color="Crash Count"),
            title="Heatmap: Crashes by Day and Hour",
            aspect="auto"
        )
        fig4 = style_fig(fig4, height=500)
    else:
        fig4 = style_fig(px.imshow([[0]]), height=300)

    # ===============================
    # 5. Map Plot (Latitude/Longitude)
    # ===============================
    if "latitude" in filtered.columns and "longitude" in filtered.columns:
        map_df = filtered.dropna(subset=["latitude", "longitude"]).head(2000)
        fig5 = px.scatter_mapbox(
            map_df,
            lat="latitude",
            lon="longitude",
            zoom=9,
            height=500,
            title="Crash Density Map (Sample)",
        )
        fig5.update_layout(mapbox_style="carto-darkmatter")
        fig5 = style_fig(fig5, height=500)
    else:
        fig5 = style_fig(px.scatter())

    # ===============================
    # 6. Pie: Injury Breakdown
    # ===============================
    injury_counts = {
        "Pedestrians Injured": filtered["number_of_pedestrians_injured"].sum(),
        "Cyclists Injured": filtered["number_of_cyclist_injured"].sum(),
        "Motorists Injured": filtered["number_of_motorist_injured"].sum()
    }
    fig6 = style_fig(
        px.pie(
            values=list(injury_counts.values()),
            names=list(injury_counts.keys()),
            title="Injury Breakdown"
        )
    )

    # ===============================
    # 7. Vehicle Type Distribution
    # ===============================
    veh_counts = (
        filtered["vehicle_type_code1"].fillna("UNKNOWN").value_counts().head(15).reset_index()
    )
    veh_counts.columns = ["vehicle_type", "count"]
    fig7 = style_fig(
        px.bar(veh_counts, x="vehicle_type", y="count",
               title="Top Vehicle Types Involved")
    )

    # ===============================
    # 8. Severity Chart (Injuries vs Fatalities)
    # ===============================
    severity = pd.DataFrame({
        "Category": ["Injured", "Killed"],
        "Count": [
            filtered["number_of_persons_injured"].sum(),
            filtered["number_of_persons_killed"].sum()
        ]
    })
    fig8 = style_fig(
        px.bar(severity, x="Category", y="Count",
               title="Crash Severity (Injured vs Killed)")
    )

    return render_template(
        "index.html",
        boroughs=["All"] + BOROUGHS,
        years=["All"] + [str(y) for y in YEARS],
        vehicles=["All"] + VEH_TYPES,
        factors=["All"] + FACTORS,
        injuries=INJURY_TYPES,
        fig1=fig1.to_html(full_html=False, include_plotlyjs="cdn"),
        fig2=fig2.to_html(full_html=False, include_plotlyjs=False),
        fig3=fig3.to_html(full_html=False, include_plotlyjs=False),
        fig4=fig4.to_html(full_html=False, include_plotlyjs=False),
        fig5=fig5.to_html(full_html=False, include_plotlyjs=False),
        fig6=fig6.to_html(full_html=False, include_plotlyjs=False),
        fig7=fig7.to_html(full_html=False, include_plotlyjs=False),
        fig8=fig8.to_html(full_html=False, include_plotlyjs=False),
    )


if __name__ == "__main__":
    app.run(debug=True)
