# Algorithms And Big Data in Chemistry
This project was made for learning purposes: how to work with given set of data from a data-driven perspective
The data we got contains next features:
- DOI, date, journal, title
- Name
- measurement_error
- measurement_wavelength
- measurement_method
- normalised_name
- raw_value
- specifier

Column 'raw_value' (refractive index)  is our target feature.
## Homework 1
For the first step, we needed to extract more than 1000 descriptors and perform data cleansing steps (validation, handling of missing values, detection of outliers, handling of duplicates, data transformation and normalization). 

We preproccesed the dataset (by cleansing columns related to scientific paper), removed duplicates by column 'Name' and then gained SMILES. 

Next we parsed ~2000 descriptors from PubChem, RdKit, Material Studio Project and Mordred. 

Finally we handled missing values with KNNImputer and then normalised our data.
## Homework 2
The second step contains visualisation of our data, performing statistical analisys, calculation of correlation coefficients and implementing of linear and non-linear dimension reduction method
## Homework 3
Finally we needed to perform clustering algorithm, visualize and interpret our results. Then, apply automated feature engineering algorithms and automated feature selection in the context of machine learning problem
