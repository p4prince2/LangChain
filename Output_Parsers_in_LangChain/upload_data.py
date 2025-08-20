import os
from huggingface_hub import HfApi

api = HfApi(token=os.getenv("HF_TOKEN"))

api.upload_large_folder(
    folder_path=r"C:\Users\p4pri\OneDrive\Desktop\Data Science\data set\Fer2013",
    repo_id="Sabudh-Foundation-2018/Fer2013",
    repo_type="dataset",
)
