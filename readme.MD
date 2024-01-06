# Continuous integration (CI) - Deployment continuous (CD) for Machine Learning solutions

#add optuna
#add sklearn pipeline
#authenticate mlflow
#pandera
--

pre-commit install

dvc init
dvc add <file>
dvc remote add --default <name> gdrive://<folder ID>
dvc remote modify drive gdrive_acknowledge_abuse true
dvc push

pip-compile
pip-sync

mlflow server --backend-store-uri sqlite:///mlflow.db

mlflow server --host 0.0.0.0 --port 8888 --backend-store-uri sqlite:///mlflow.db

curl -X 'POST' \
  'http://127.0.0.1:8000/model/keras1?data_path=airflow%5Cdags%5Cdata_staging%5Ctransform%5Ctransform_house_rent_dataset.csv&token=jessica' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "learning_rate": 0,
  "epochs": 5,
  "loss": "string",
  "optimizer": "string"
}'

--
BHK: Number of Bedrooms, Hall, Kitchen.

Rent: Rent of the Houses/Apartments/Flats.

Size: Size of the Houses/Apartments/Flats in Square Feet.

Floor: Houses/Apartments/Flats situated in which Floor and Total Number of Floors (Example: Ground out of 2, 3 out of 5, etc.)

Area Type: Size of the Houses/Apartments/Flats calculated on either Super Area or Carpet Area or Build Area.

Area Locality: Locality of the Houses/Apartments/Flats.

City: City where the Houses/Apartments/Flats are Located.

Furnishing Status: Furnishing Status of the Houses/Apartments/Flats, either it is Furnished or Semi-Furnished or Unfurnished.

Tenant Preferred: Type of Tenant Preferred by the Owner or Agent.

Bathroom: Number of Bathrooms.

Point of Contact: Whom should you contact for more information regarding the Houses/Apartments/Flats.
