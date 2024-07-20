import tensorflow as tf
from tensorflow import keras
import pandas as pd

# Load and preprocess data
data = pd.read_csv('gs://your-bucket/sensor_data.csv')
train_data = data[['temperature', 'vibration']]
train_labels = data['failure']

# Build the model
model = keras.Sequential([
    keras.layers.Dense(16, activation='relu', input_shape=(train_data.shape[1],)),
    keras.layers.Dense(8, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_data, train_labels, epochs=10, batch_size=32)

# Save the model
model.save('gs://your-bucket/predictive_model.h5')
