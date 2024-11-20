import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("cleaned.csv")

# Filter columns for each year
y2004 = df.filter(regex=".*2004").columns
y2009 = df.filter(regex=".*2009").columns
y2014 = df.filter(regex=".*2014").columns
y2019 = df.filter(regex=".*2019").columns
y2024 = df.filter(regex=".*2024").columns


# Prepare the data for Prophet
def prepare_prophet_data(df, year_columns, year):
    data = df[year_columns].copy()
    data.columns = [col.replace(f"_{year}", "") for col in data.columns]
    print(data.columns)
    data["ds"] = pd.to_datetime(f"{year}-01-01")
    return data


# Combine data for all years
prophet_data = pd.concat(
    [
        prepare_prophet_data(df, y2004, 2004),
        prepare_prophet_data(df, y2009, 2009),
        prepare_prophet_data(df, y2014, 2014),
        prepare_prophet_data(df, y2019, 2019),
        # prepare_prophet_data(df, y2024, 2024),
    ]
)

model = Prophet()
prophet_data.to_csv("prophet_data.csv", index=False)
prophet_data.rename(columns={"Party": "y"})
model.add_regressor("State")
model.add_regressor("Electors")
model.add_regressor("Votes")
model.add_regressor("Turnout")
model.add_regressor("Margin")
model.add_regressor("Margin %")
model.fit(prophet_data)

prophet_data.to_csv("prophet_data.csv", index=False)


model = Prophet()
model.fit(prophet_data)

# # Make future predictions
future = model.make_future_dataframe(periods=365)
future[y2024] = df[y2024]
future.columns = [col.replace(f"_2024", "") for col in future.columns]
forecast = model.predict(future)

# # Print the forecast
print(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]])
