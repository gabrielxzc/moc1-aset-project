# THIS IS JUST AN EXAMPLE. IT WILL NOT RUN

# https://medium.com/@aditya.gogoi.30aug/deep-learning-for-predicting-stock-prices-1088534c683f
# https://finance.yahoo.com/quote/GOOG/history?period1=1092862800&period2=1570050000&interval=1d&filter=history&frequency=1d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

training_set = pd.read_csv('../google_stock_data/train_data.csv')
training_set = training_set.iloc[:, 1:2].values
sc = MinMaxScaler()
training_set = sc.fit_transform(training_set)
X_train = training_set[0:-14]
y_train = training_set[14:]
X_train = np.reshape(X_train, (len(X_train), 1, 1))
regressor = Sequential()
regressor.add(LSTM(units=4, activation='sigmoid', input_shape=(None, 1)))
regressor.add(Dense(units=1))
regressor.compile(optimizer='adam', loss='mean_squared_error')
regressor.fit(X_train, y_train, batch_size=32, epochs=200)
test_set = pd.read_csv('../google_stock_data/test_data.csv')
real_stock_price = test_set.iloc[:, 1:2].values
inputs = real_stock_price
inputs = sc.transform(inputs)
inputs = np.reshape(inputs, (65, 1, 1))
predicted_stock_price = regressor.predict(inputs)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)
plt.plot(real_stock_price, color='red', label='Real Google Stock Price')
plt.plot(predicted_stock_price, color='blue', label='Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()