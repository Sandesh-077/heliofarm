import pickle
import pandas as pd

# Load the SARIMAX model
with open('sarimax_model.pkl', 'rb') as file:
    model_fit = pickle.load(file)

def make_prediction(exog):
    # Generate predictions
    forecast = model_fit.get_forecast(steps=15, exog=exog)
    return forecast.predicted_mean

def get_user_input():
    # Get latitude and longitude from the user
    latitude = float(input("Enter Latitude: "))
    longitude = float(input("Enter Longitude: "))
    
    # Get external factors from the user
    t_2m = float(input("Enter Temperature (°C): "))
    precip_1h = float(input("Enter Precipitation (mm): "))
    wind_speed_10m = float(input("Enter Wind Speed (m/s): "))
    relative_humidity_2m = float(input("Enter Relative Humidity (fraction): "))
    total_cloud_cover = float(input("Enter Total Cloud Cover (octas): "))
    
    # Create a DataFrame for the external factors
    exog_data = pd.DataFrame({
        't_2m:C': [t_2m],
        'precip_1h:mm': [precip_1h],
        'wind_speed_10m:ms': [wind_speed_10m],
        'relative_humidity_2m:p': [relative_humidity_2m],
        'total_cloud_cover:octas': [total_cloud_cover]
    })
    
    return latitude, longitude, exog_data

if __name__ == "__main__":
    # Get user input
    latitude, longitude, exog = get_user_input()
    
    # Make predictions
    predictions = make_prediction(exog)
    
    # Display the predictions
    print(f"\nPredicted Solar Radiation for the next 15 days at Latitude {latitude} and Longitude {longitude}:")
    for i, pred in enumerate(predictions):
        print(f"Day {i + 1}: {pred:.2f} W/m²")
