"""
This script fetches and analyzes historical weather data for a specific
location over the last 7 days using the Open-Meteo API.

It performs the following actions:
1. Retrieves daily maximum and minimum temperatures.
2. Prints the weather records.
3. Identifies the highest and lowest temperatures and their corresponding dates.
4. Spots anomalies by comparing daily maximum temperatures to the historical
   average for this time of year.
"""

import requests
import pandas as pd
from datetime import date, timedelta

# --- Constants ---
# Coordinates for Hyderabad, Telangana, India
HYDERABAD_LAT = 17.3850
HYDERABAD_LON = 78.4867

# Historical average max temperature for Hyderabad in late August is ~29.6°C.
# Source: India Meteorological Department (1991-2020 data)
HISTORICAL_AVG_MAX_TEMP_C = 29.6
# We'll define an anomaly as a day where the max temperature is more
# than 2.5°C different from the historical average.
ANOMALY_THRESHOLD_C = 2.5


def get_weather_data(latitude, longitude, days=7):
    """
    Fetches historical weather data for a given location.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        days (int): The number of past days for which to retrieve data.

    Returns:
        pandas.DataFrame: A DataFrame containing the weather data,
                          or None if an error occurs.
    """
    try:
        end_date = date.today()
        start_date = end_date - timedelta(days=days - 1)
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")

        api_url = (
            "https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={latitude}&longitude={longitude}&"
            f"start_date={start_date_str}&end_date={end_date_str}&"
            "daily=temperature_2m_max,temperature_2m_min&"
            "timezone=auto"
        )

        print(f"Fetching data from: {api_url}\n")
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if 'daily' not in data:
            print("Error: 'daily' data not found in the API response.")
            return None

        df = pd.DataFrame(data['daily'])
        df.rename(columns={
            'time': 'date',
            'temperature_2m_max': 'max_temp_celsius',
            'temperature_2m_min': 'min_temp_celsius'
        }, inplace=True)
        df['date'] = pd.to_datetime(df['date'])
        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def analyze_weather_data(df):
    """
    Analyzes weather data to find key statistics and anomalies.

    Args:
        df (pandas.DataFrame): The DataFrame containing weather data.
    """
    if df is None or df.empty:
        print("No data available to analyze.")
        return

    print("--- Weather Records for the Last 7 Days ---")
    print(df.to_string(index=False))
    print("\n" + "=" * 50 + "\n")

    # --- Find Highest and Lowest Temperatures ---
    highest_temp_record = df.loc[df['max_temp_celsius'].idxmax()]
    highest_temp = highest_temp_record['max_temp_celsius']
    date_of_highest_temp = highest_temp_record['date'].strftime('%Y-%m-%d')

    lowest_temp_record = df.loc[df['min_temp_celsius'].idxmin()]
    lowest_temp = lowest_temp_record['min_temp_celsius']
    date_of_lowest_temp = lowest_temp_record['date'].strftime('%Y-%m-%d')

    print("--- Temperature Extremes ---")
    print(f"Highest Temperature Recorded: {highest_temp}°C on {date_of_highest_temp}")
    print(f"Lowest Temperature Recorded:  {lowest_temp}°C on {date_of_lowest_temp}")
    print("\n" + "=" * 50 + "\n")

    # --- Spot Anomalies ---
    print("--- Anomaly Detection ---")
    print(f"Comparing against historical average max temp of {HISTORICAL_AVG_MAX_TEMP_C}°C "
          f"for this time of year.")
    print(f"An anomaly is a day with a max temp > {ANOMALY_THRESHOLD_C}°C "
          "from the average.\n")

    # Calculate the deviation from the historical average for each day
    df['deviation'] = df['max_temp_celsius'] - HISTORICAL_AVG_MAX_TEMP_C

    # Filter for days that meet the anomaly criteria
    anomalies = df[abs(df['deviation']) > ANOMALY_THRESHOLD_C]

    if not anomalies.empty:
        for _, row in anomalies.iterrows():
            day_date = row['date'].strftime('%Y-%m-%d')
            day_temp = row['max_temp_celsius']
            deviation = row['deviation']

            if deviation > 0:
                print(
                    f"-> Unusually HOT day on {day_date}: "
                    f"Max temp was {day_temp}°C, which is {deviation:.2f}°C "
                    "ABOVE the historical average."
                )
            else:
                print(
                    f"-> Unusually COLD day on {day_date}: "
                    f"Max temp was {day_temp}°C, which is {abs(deviation):.2f}°C "
                    "BELOW the historical average."
                )
    else:
        print("No unusually hot or cold days were detected in the last 7 days.")


def main():
    """Main function to execute the script."""
    weather_df = get_weather_data(HYDERABAD_LAT, HYDERABAD_LON)
    if weather_df is not None:
        analyze_weather_data(weather_df)


if __name__ == "__main__":
    main()
