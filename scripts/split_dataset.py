from pathlib import Path
import shutil
import random
random.seed(42)
RAW_DATASET_PATH = Path("data/raw/lung_colon_image_set/colon_image_sets")
PROCESSED_DATASET_PATH = Path("data/processed")
class_folders = [folder for folder in RAW_DATASET_PATH.iterdir() if folder.is_dir()]
print("Classes found:")
for folder in class_folders:
    print(f"- {folder.name}")
for folder in class_folders:
    (PROCESSED_DATASET_PATH / "train" / folder.name).mkdir(parents=True, exist_ok=True)
    (PROCESSED_DATASET_PATH / "validation" / folder.name).mkdir(parents=True, exist_ok=True)
    (PROCESSED_DATASET_PATH / "test" / folder.name).mkdir(parents=True, exist_ok=True)
for folder in class_folders:
    image_files = list(folder.iterdir())
    random.shuffle(image_files)
    train_split = int(0.8*len(image_files))
    validation_split = int(0.9*len(image_files))
    train_images = image_files[:train_split]
    validation_images = image_files[train_split:validation_split]
    test_images = image_files[validation_split:]
    for image in train_images:
        shutil.copy2(image, PROCESSED_DATASET_PATH/ "train" / folder.name)
    for image in validation_images:
        shutil.copy2(image, PROCESSED_DATASET_PATH / "validation" / folder.name)
    for image in test_images:
        shutil.copy2(image, PROCESSED_DATASET_PATH / "test" / folder.name)


