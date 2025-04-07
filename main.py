import os
from download_models import download_models

def main():
    model_dir = "models"
    if not os.path.exists(model_dir) or not os.listdir(model_dir):
        download_models()

if __name__ == "__main__":
    main()
