import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

NUM_HIDDEN_NEURONS = 28
LEARNING_RATE = 0.1
EPOCHS = 20

TRAINING_PERCENT = 0.7
VALIDATION_PERCENT = 0.1
TEST_PERCENT = 0.2

INPUT_SIZE = 784
OUTPUT_SIZE = 10


def read_data():
    #ovdje citas vrijednosti iz fajla
    data = pd.read_csv('assignment5.csv')
    #normalising data deviding it with 255 and ignoring the label column
    x_data = data.drop('label', axis=1).values / 255

    #Storing label column into y_data
    y_data = data['label'].values

    #calculating how mhch of training and validations size
    train_size = int(TRAINING_PERCENT * len(data))
    val_size = int(VALIDATION_PERCENT * len(data))


    #reading the data into odgovarajuce variables
    train_x = x_data[:train_size]
    val_x = x_data[train_size:train_size + val_size]
    test_x = x_data[train_size + val_size:]

    #reading the labes into designated variables
    train_y = y_data[:train_size]
    val_y = y_data[train_size:train_size + val_size]
    test_y = y_data[train_size + val_size:]

    return train_x, train_y, val_x, val_y, test_x, test_y


# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def format_output(y):
    #formatting the output by turning the list inth ot encoded matrix
    formatted = np.zeros((len(y), 10))
    for i, label in enumerate(y):
        formatted[i][label] = 1.0
    return formatted


def initialize_weights(input_size, hidden_size, output_size):
    #postavi weights na random broj između -0.5 i .5
    w_i_h = np.random.uniform(-0.5, 0.5, (hidden_size, input_size))
    w_h_o = np.random.uniform(-0.5, 0.5, (output_size, hidden_size))

    #postavi baises na 0
    b_i_h = np.zeros((hidden_size, 1))
    b_h_o = np.zeros((output_size, 1))
    return w_i_h, w_h_o, b_i_h, b_h_o


def forward_propagation(img, w_i_h, w_h_o, b_i_h, b_h_o):
    #do the forward propagation with formulas and activation functions
    h_pre = b_i_h + w_i_h @ img
    h = sigmoid(h_pre)
    o_pre = b_h_o + w_h_o @ h
    o = sigmoid(o_pre)
    return h, o


def backpropagation(img, h, o, label, w_i_h, w_h_o, b_i_h, b_h_o):
    #backpropagation, updejting weights i biases za hidden-output level
    delta_o = o - label
    w_h_o -= LEARNING_RATE * delta_o @ h.T
    b_h_o -= LEARNING_RATE * delta_o

    #updejting weights i biases za input-hidden level
    delta_h = w_h_o.T @ delta_o * sigmoid_derivative(h)
    w_i_h -= LEARNING_RATE * delta_h @ img.T
    b_i_h -= LEARNING_RATE * delta_h

    return w_i_h, w_h_o, b_i_h, b_h_o


def train(train_x, train_y, w_i_h, w_h_o, b_i_h, b_h_o):
    train_y = format_output(train_y)
    num_correct = 0

    #print(test_y)

    for epoch in range(EPOCHS):
        for img, label in zip(train_x, train_y):
            #reshape the images
            img = img.reshape(-1, 1)
            label = label.reshape(-1, 1)

            h, o = forward_propagation(img, w_i_h, w_h_o, b_i_h, b_h_o)
            num_correct += int(np.argmax(o) == np.argmax(label))
            #print(num_correct)

            w_i_h, w_h_o, b_i_h, b_h_o = backpropagation(img, h, o, label, w_i_h, w_h_o, b_i_h, b_h_o)

        print(f"Epoch {epoch + 1} Accuracy: {round((num_correct / len(train_x)) * 100, 2)}%")
        num_correct = 0

    return w_i_h, w_h_o, b_i_h, b_h_o


def test(test_x, test_y, w_i_h, w_h_o, b_i_h, b_h_o):
    #testing function
    num_correct = 0
    test_y = format_output(test_y)

    for img, label in zip(test_x, test_y):

        img = img.reshape(-1, 1)
        label = label.reshape(-1, 1)

        useless_variable, o = forward_propagation(img, w_i_h, w_h_o, b_i_h, b_h_o)
        num_correct += int(np.argmax(o) == np.argmax(label))
        #print(num_correct)

    print(f"Test Accuracy: {round((num_correct / len(test_x)) * 100, 2)}%")


def predict_and_visualize(test_x, w_i_h, w_h_o, b_i_h, b_h_o):
    #ova funkcija samo uzme broj iz dataseta, plota ga i kaze da li je program pogodio broj
    while True:
        index = int(input("Enter a number (0 - 9999): "))
        img = test_x[index]
        plt.imshow(img.reshape(28, 28), cmap="Greys")

        img = img.reshape(-1, 1)
        useless_variable, o = forward_propagation(img, w_i_h, w_h_o, b_i_h, b_h_o)

        plt.title(f"Prediction: {np.argmax(o)}")
        plt.show()


# Main execution
train_x, train_y, val_x, val_y, test_x, test_y = read_data()
w_i_h, w_h_o, b_i_h, b_h_o = initialize_weights(784, NUM_HIDDEN_NEURONS, 10)

print("Training started...")
w_i_h, w_h_o, b_i_h, b_h_o = train(train_x, train_y, w_i_h, w_h_o, b_i_h, b_h_o)
print("Training completed!")

test(test_x, test_y, w_i_h, w_h_o, b_i_h, b_h_o)
predict_and_visualize(test_x, w_i_h, w_h_o, b_i_h, b_h_o)
