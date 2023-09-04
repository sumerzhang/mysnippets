import argparse

# Define and parse command line arguments
parser = argparse.ArgumentParser(
    prog='Model Training',
    description='Train a model on some data.',
    epilog='Enjoy the program! :)'
)

# Add positional arguments
parser.add_argument('train_data', help='Training data file.')

# Add optional arguments
parser.add_argument('-e', '--epochs', type=int, default=10,
                    help='Number of epochs to train the model.')

#parse the arguments
args = parser.parse_args()
print(args)