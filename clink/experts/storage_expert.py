import pickle


def save_object(path, obj):
    with open(path, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load(path):
    with open(path, 'rb') as handle:
        return pickle.load(handle)
