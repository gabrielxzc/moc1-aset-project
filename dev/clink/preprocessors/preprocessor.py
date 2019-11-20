class Preprocessor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def preprocess(self):
        """
        :return: A tuple with two elements: (x_processed, y_processed)
        containing the processed inputs.
        """
        raise NotImplementedError()

    def postprocess(self, x_raw, x_processed, prediction):
        raise NotImplementedError()
