import aspectlib
import numpy as np

@aspectlib.Aspect(bind = True)
def log_call(cutpoint, *args, **kargs):
	with open("calls.txt", "a") as out_file:
		out_file.write(str(cutpoint.__name__) + "\n")
	yield

@aspectlib.Aspect
def validate_extension(*args, **kargs):
	sound_path = kargs['sound_path']
	assert sound_path[-4:] == ".wav"
	yield

@aspectlib.Aspect
def validate_return_value(*args, **kargs):
	val = yield aspectlib.Proceed
	assert isinstance(val, np.ndarray)
