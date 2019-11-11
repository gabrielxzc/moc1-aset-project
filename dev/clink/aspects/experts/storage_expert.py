import aspectlib


@aspectlib.Aspect
def save_object_aspect(*args):
    print("Storage expert saving new object at path %s" % args[0])
    yield
    print("Storage expert successfully saved object!")


@aspectlib.Aspect
def load_aspect(*args):
    print("Storage expert loading object from path %s" % args[0])
    yield
    print("Storage expert successfully loaded object!")
