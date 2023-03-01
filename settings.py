import os

def path_to_data_file(path):
    cur_dir = os.path.dirname(os.path.realpath(__file__))

    return os.path.normpath(os.path.join(cur_dir, path))

DATA_FILE = path_to_data_file('../data.csv')
TRAIN_FILE = path_to_data_file('../train_data.csv')
TEST_FILE = path_to_data_file('../test_data.csv')