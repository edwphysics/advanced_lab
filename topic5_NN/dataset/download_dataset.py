import kagglehub

# Download latest version
path = kagglehub.dataset_download("ahmadbader17/fighter-planes-classification-dataset")

print("Path to dataset files:", path)