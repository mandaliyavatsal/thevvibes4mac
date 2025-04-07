import os
from huggingface_hub import hf_hub_download

def download_models():
    model_ids = [
        "openai/whisper-small",
        "facebook/wav2vec2-base-960h"
    ]
    model_dir = "models"

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    for model_id in model_ids:
        try:
            model_path = hf_hub_download(repo_id=model_id, filename="pytorch_model.bin", cache_dir=model_dir)
            print(f"Downloaded {model_id} to {model_path}")
        except Exception as e:
            print(f"Failed to download {model_id}: {e}")

if __name__ == "__main__":
    download_models()
