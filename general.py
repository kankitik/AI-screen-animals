from tensorflow.keras.utils import get_file

url = "https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip"
path_to_zip = get_file('cats_and_dogs.zip', origin=url, extract=True)



