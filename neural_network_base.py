import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

class TradingNeuralNetwork:
    def __init__(self, input_shape=(10,)):
        """
        Initialize the neural network model for trading analysis.
        
        Args:
            input_shape (tuple): Shape of the input data (default is (10,) for 10 features).
        """
        self.model = self._create_model(input_shape)

    def _create_model(self, input_shape):
        """
        Create a neural network model for trading analysis.
        
        Args:
            input_shape (tuple): Shape of the input data.
        
        Returns:
            tf.keras.Model: The compiled neural network model.
        """
        model = models.Sequential()
        
        # Input layer
        model.add(layers.InputLayer(input_shape=input_shape))
        
        # First hidden layer with dropout
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dropout(0.3))  # Dropout layer to reduce overfitting
        
        # Second hidden layer with dropout
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dropout(0.3))
        
        # Third hidden layer
        model.add(layers.Dense(32, activation='relu'))
        
        # Fourth hidden layer with L2 regularization
        model.add(layers.Dense(16, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
        
        # Output layer with sigmoid for classification
        model.add(layers.Dense(1, activation='sigmoid'))  # Binary classification: Buy or Sell

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, epochs=20, batch_size=32, validation_data=None):
        """
        Train the neural network model with additional validation data.
        
        Args:
            X_train (ndarray): Training features.
            y_train (ndarray): Training labels (buy/sell or performance score).
            epochs (int): Number of epochs to train.
            batch_size (int): Size of each batch during training.
            validation_data (tuple): Validation data (X_val, y_val).
        """
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=validation_data)

    def evaluate(self, X_test, y_test):
        """
        Evaluate the model on the test set.
        
        Args:
            X_test (ndarray): Test features.
            y_test (ndarray): Test labels.
        
        Returns:
            tuple: Test loss and accuracy.
        """
        return self.model.evaluate(X_test, y_test)

    def predict(self, X):
        """
        Predict the output for a given input.
        
        Args:
            X (ndarray): Input data to predict on.
        
        Returns:
            ndarray: Predicted results.
        """
        return self.model.predict(X)

    def save_model(self, filepath='trading_model.h5'):
        """
        Save the trained model to a file.
        
        Args:
            filepath (str): Path to save the model.
        """
        self.model.save(filepath)

    def load_model(self, filepath='trading_model.h5'):
        """
        Load a pre-trained model from a file.
        
        Args:
            filepath (str): Path to the model file.
        """
        self.model = models.load_model(filepath)

# Example usage:
if __name__ == "__main__":
    # Generate some fake data for illustration
    X_train = np.random.rand(1000, 20)  # 1000 samples with 20 features each
    y_train = np.random.randint(2, size=1000)  # Binary labels (buy/sell)

    # Initialize and train the model
    nn = TradingNeuralNetwork(input_shape=(20,))
    nn.train(X_train, y_train, epochs=20)

    # Evaluate the model
    X_test = np.random.rand(200, 20)
    y_test = np.random.randint(2, size=200)
    test_loss, test_acc = nn.evaluate(X_test, y_test)
    print(f"Test Loss: {test_loss}, Test Accuracy: {test_acc}")
