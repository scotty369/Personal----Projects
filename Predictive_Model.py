import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Function to load datasets and check for 'key' column
def load_and_merge_data():
    # Load datasets
    offender = pd.read_csv('Offender.csv')
    victim = pd.read_csv('Victim.csv')
    location = pd.read_csv('Location.csv')
    relationship = pd.read_csv('Relationship.csv')
    weapon = pd.read_csv('Weapon.csv')
    offense = pd.read_csv('Offense.csv')

    # Check if 'key' column exists in each DataFrame
    for df_name, df in zip(['Offender', 'Victim', 'Location', 'Relationship', 'Weapon', 'Offense'],
                            [offender, victim, location, relationship, weapon, offense]):
        if 'key' not in df.columns:
            print(f"'{df_name}' DataFrame is missing 'key' column. Columns are: {df.columns.tolist()}")

    # Merge datasets on 'key' column
    merged_data = (offender.merge(victim, on='key', suffixes=('_offender', '_victim'))
                          .merge(location, on='key')
                          .merge(relationship, on='key')
                          .merge(weapon, on='key')
                          .merge(offense, on='key'))
    
    return merged_data

# Preprocess and encode data
def preprocess_data(merged_data):
    # Fill missing values
    merged_data.fillna('Unknown', inplace=True)

    # Encode categorical variables
    label_encoders = {}
    for column in ['key', 'Offender Age', 'Victim Age', 'Location Type', 'Relationship', 'Weapon', 'Offense']:
        le = LabelEncoder()
        merged_data[column] = le.fit_transform(merged_data[column].astype(str))
        label_encoders[column] = le

    return merged_data, label_encoders

# Function to build and train the model
def train_model(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(np.unique(y)), activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

    y_pred = np.argmax(model.predict(X_test), axis=-1)
    accuracy = accuracy_score(y_test, y_pred)

    return history, accuracy

# Function to plot training results
def plot_results(history):
    plt.figure(figsize=(12, 4))
    
    # Accuracy plot
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    # Loss plot
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

# Main execution flow
if __name__ == "__main__":
    # Load and merge data
    merged_data = load_and_merge_data()

    # Preprocess the merged data
    model_df, label_encoders = preprocess_data(merged_data)

    # Define features and target variable
    X = model_df[['Offender Age', 'Victim Age', 'Location Type', 'Relationship', 'Weapon']]
    y = model_df['Offense']

    # Train the model and get the results
    history, accuracy = train_model(X, y)

    print(f'Model Accuracy: {accuracy:.2f}')

    # Plot training results
    plot_results(history)

    print("\nModel training and evaluation completed.")
