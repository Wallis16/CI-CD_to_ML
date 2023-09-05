import gdown

# a file
url = "https://drive.google.com/file/d/1LZMr1vN6girXHu8PX1OOLb5MJUXthdEB/view?usp=sharing"
output = "house_rent_dataset.csv"
gdown.download(url=url, output=output, quiet=False, fuzzy=True)