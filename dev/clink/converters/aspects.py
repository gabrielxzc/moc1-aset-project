import aspectlib
import numpy as np
import time

@aspectlib.Aspect(bind = True)
def log_call(cutpoint, *args, **kargs):
	with open("calls.txt", "a") as out_file:
		out_file.write(str(time.time()) + " " + str(cutpoint.__name__) + "\n")
	yield

@aspectlib.Aspect
def validate_extension(*args, **kargs):
	if 'sound_path' in kargs:
		sound_path = kargs['sound_path']
		assert len(sound_path) >= 4 and sound_path[-4:] == ".wav"
	yield

@aspectlib.Aspect
def validate_return_value(*args, **kargs):
	val = yield aspectlib.Proceed
	assert isinstance(val, np.ndarray)
