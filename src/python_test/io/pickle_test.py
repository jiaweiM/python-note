import pickle
import os


def test():
    path = 'mydata.pickle'
    with open(path, "wb") as saved_data:
        pickle.dump([1, 2, 3, "data"], saved_data)

    with open(path, 'rb') as restored_data:
        lst = pickle.load(restored_data)
        assert lst == [1, 2, 3, "data"]
    os.remove(path)
