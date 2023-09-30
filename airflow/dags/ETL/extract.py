import gdown

def download_from_drive(url: str, output_name: str, data_staging_path: str) -> str:

    gdown.download(url=url, output=data_staging_path+output_name, quiet=False, fuzzy=True)
    return data_staging_path+output_name
