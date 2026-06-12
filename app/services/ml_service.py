from sklearn.linear_model import LinearRegression
import numpy as np

def predict_admissions(historical_data):

    totals = []

    for row in historical_data:

        total = row["total"]
        year = row["academic_year"]

        if total <= 20:
            continue

        if year == "8193-8194":
            continue

        if total > 1000:
            continue

        totals.append(total)

    print("CLEANED TOTALS =", totals)

    X = np.array(range(len(totals))).reshape(-1, 1)
    y = np.array(totals)

    model = LinearRegression()
    model.fit(X, y)

    prediction = round(
        model.predict([[len(totals)]])[0]
    )

    growth = round(
        ((prediction - totals[-1]) / totals[-1]) * 100,
        2
    )

    if growth <= 5:
        trend = "Stable"
    elif growth <= 20:
        trend = "Moderate Growth"
    else:
        trend = "High Growth"

    return {
        "predicted_admissions": prediction,
        "growth_status": trend
    }