from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image
import random
DATASET_PATH = Path("data/raw/lung_colon_image_set/colon_image_sets")
print(f"Dataset location: {DATASET_PATH}")
if DATASET_PATH.exists():
    print("Dataset found!")
else:
    print("Dataset not found.")
class_folders = [folder for folder in DATASET_PATH.iterdir() if folder .is_dir()]
for folder in class_folders:
    print(f"- {folder.name}")
print("\nImage count per class:")
for folder in class_folders:
    image_count = len(list(folder.iterdir()))
    print(f"{folder.name}: {image_count} images")
print("\nDisplaying 6 random images from each class...")
for folder in class_folders:
    image_files = list(folder.iterdir())
    sample_images = random.sample(image_files,6)
    fig,axes = plt.subplots(2,3,figsize=(8,6))
    fig.suptitle(folder.name, fontsize=16)
    for ax,image_path in zip(axes.flat, sample_images):
        image = Image.open(image_path)
        ax.imshow(image)
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(1)
            spine.set_edgecolor("black")
        ax.set_xticks([])
        ax.set_yticks([])
    plt.tight_layout(rect=[0,0,1,0.95], pad=3)
    plt.show()