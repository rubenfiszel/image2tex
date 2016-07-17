from keras.models import model_from_json
import numpy as np
import pickle


def load_model(arch = 'model_architecture.json',
			   weights = 'model_weights.h5',
			   labels_pickle = 'labels.pkl'):
	
	"""Summary: Load a saved model and labels.
	
	Args:
	    arch (str, optional): Path to model architecture json
	    weights (str, optional): Path to saved weights of model
	    labels_pickle (str, optional): Loaded pickle of labels
	
	Returns:
	    Keras model, Numpy array of labels
	"""
	model = model_from_json(open(arch).read())
	model.load_weights(weights)
	labels = np.array(pickle.load(open(labels_pickle)))

	return model, labels



def model_eval(input, model, labels):
	
	"""Summary: Evalute a numpy array through the model.
	
	Args:
	    input (Numpy Array): Array with shape (batch_size, 1, 28, 28)
	    model (Keras model): Loaded keras model from load_model()
	    labels (Numpy Array): Array of labels from load_model
	
	Returns:
	    Numpy Array: Array of predicted labels.
	"""

	predictions = model.predict_classes(input, batch_size = len(input), verbose=0)
	labeled_predictions = labels[predictions]

	return labeled_predictions