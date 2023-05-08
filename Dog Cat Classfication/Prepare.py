import zipfile
import os
import shutil

# Open the zip file for reading
with zipfile.ZipFile('dogs-vs-cats.zip', 'r') as zip_ref:
    # Extract all contents to the current directory
    zip_ref.extractall('.')
    
    
with zipfile.ZipFile('train.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

    
    
with zipfile.ZipFile('test1.zip', 'r') as zip_ref:
    zip_ref.extractall('.')
    
    


new_cats_dir = os.path.join('train', 'Cats')
new_dogs_dir = os.path.join('train', 'Dogs')

os.makedirs(new_cats_dir)
os.makedirs(new_dogs_dir)


# Preparing the train data by adding all cats photos to folder named Cats, same with dogs
for filename in os.listdir('train'):
    
    # If cat image
    if filename.startswith('cat'):
        src_path = os.path.join('train', filename)  
        dest_path = os.path.join(new_cats_dir, filename)
        # Move the file to the new directory
        shutil.move(src_path, dest_path)
    
    # if dog image
    if filename.startswith('dog'):
        src_path = os.path.join('train', filename)
        dest_path = os.path.join(new_dogs_dir, filename)
        # Move the file to the new directory
        shutil.move(src_path, dest_path)



# Moving all the test data to sub Folder called all, so we can load them in pytorch
all_folder_path = os.path.join('test1', "all")
os.makedirs(all_folder_path)

for filename in os.listdir('test1'):
    file_path = os.path.join('test1', filename)

    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Move the image to the "all" subfolder
        shutil.move(file_path, all_folder_path)

os.remove('train.zip')
os.remove('test1.zip')