import requests
import pandas as pd
from google.cloud import storage

def fetch_sensor_data():
    response = requests.get('http://your-aelf-node-api/sensor-data')
    data = response.json()
    df = pd.DataFrame(data)
    # Preprocess data
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['temperature'] = df['temperature'].astype(float)
    df['vibration'] = df['vibration'].astype(float)
    return df

def data_extraction(request):
    df = fetch_sensor_data()
    client = storage.Client()
    bucket = client.get_bucket('your-bucket')
    blob = bucket.blob('sensor_data.csv')
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')
    return 'Data extraction completed'
