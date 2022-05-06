import os
import pathlib
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
from IPython.display import display
from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
# patch tf1 into `utils.ops`
utils_ops.tf = tf.compat.v1
# Patch the location of gfile
tf.gfile = tf.io.gfile
# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = "C:\\Users\\derar\\Desktop\\project_graduation_images\\variables\\labelmap.pbtxt"
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=False)
# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
detection_model = tf.saved_model.load("C:\\Users\\derar\\Desktop\\project_graduation_images")
def run_inference_for_single_image(model, image):
    image = np.asarray(image)
    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis,...]
    # Run inference
    model_fn = model.signatures['serving_default']
    output_dict = model_fn(input_tensor)
    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key:value[0, :num_detections].numpy() 
    for key,value in output_dict.items()}
    output_dict['num_detections'] = num_detections
    
    return category_index[output_dict['detection_classes'][0]]['name']
    
def return_faculty_name(PATH):
    name = run_inference_for_single_image(detection_model, PATH)
    return name