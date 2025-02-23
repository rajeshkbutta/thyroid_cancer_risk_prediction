import pandas as pd

def get_all_data(file_path):
    try:
        return pd.read_csv(file_path)
    except:
        raise FileNotFoundError


def pt_identifier_removal(data):
    data.drop("Patient_ID", axis=1, inplace=True)
    return data


# def encoder(data):
#     genders = ['Male', 'Female']
#     countries = ['Russia', 'Germany', 'Nigeria', 'India', 'UK', 'South Korea', 'Brazil', 'China', 'Japan', 'USA']
#     ethnicities = ['Caucasian', 'Hispanic', 'Asian', 'African', 'Middle Eastern']
#     FHs = ['Yes', 'No']
#     radiation_exposures = ['Yes', 'No']
#     iodine_deficiencies = ['Yes', 'No']
#     smoking_encodings = ['Yes', 'No']
#     obesity_encodings = ['Yes', 'No']
#     diabetes_encodings = ['Yes', 'No']
#     thyroid_cancer_risk_encodings = ['Low', 'Medium', 'High']
#     diagnosis_encodings = ['Benign', 'Malignant']
#
#     gender_to_index = {gender: index for index, gender in enumerate(genders)}
#     country_to_index = {country: index for index, country in enumerate(countries)}
#     ethnicity_to_index = {ethnicity: index for index, ethnicity in enumerate(ethnicities)}
#     FH_to_index = {FH: index for index, FH in enumerate(FHs)}
#     radiation_exposure_to_index = {radiation_exposure: index for index, radiation_exposure in enumerate(radiation_exposures)}
#     iodine_deficiency_to_index = {iodine_deficiency: index for index, iodine_deficiency in
#                                   enumerate(iodine_deficiencies)}
#     smoking_to_index = {smoking_encoding: index for index, smoking_encoding in enumerate(smoking_encodings)}
#     obesity_to_index = {obesity_encoding: index for index, obesity_encoding in enumerate(obesity_encodings)}
#     thyroid_cancer_risk_to_index = {thyroid_cancer_risk_encoding: index for index, thyroid_cancer_risk_encoding in
#                                     enumerate(thyroid_cancer_risk_encodings)}
#     diabetes_to_index = {diabetes_encoding: index for index, diabetes_encoding in enumerate(diabetes_encodings)}
#     diagnosis_to_index = {diagnosis_encoding: index for index, diagnosis_encoding in enumerate(diagnosis_encodings)}
#
#     for row in range(data.shape[0]):
#         data.loc[row, 'Gender'] = gender_to_index[data['Gender'][row]]
#         data.loc[row, 'Country'] = country_to_index[data['Country'][row]]
#         data.loc[row, 'Thyroid_Cancer_Risk'] = thyroid_cancer_risk_to_index[data['Thyroid_Cancer_Risk'][row]]
#         data.loc[row, 'Ethnicity'] = ethnicity_to_index[data['Ethnicity'][row]]
#         data.loc[row, 'Family_History'] = FH_to_index[data['Family_History'][row]]
#         data.loc[row, 'Radiation_Exposure'] = radiation_exposure_to_index[data['Radiation_Exposure'][row]]
#         data.loc[row, 'Iodine_Deficiency'] = iodine_deficiency_to_index[data['Iodine_Deficiency'][row]]
#         data.loc[row, 'Smoking'] = smoking_to_index[data['Smoking'][row]]
#         data.loc[row, 'Obesity'] = obesity_to_index[data['Obesity'][row]]
#         data.loc[row, 'Diabetes'] = diabetes_to_index[data['Diabetes'][row]]
#         data.loc[row, 'Diagnosis'] = diagnosis_to_index[data['Diagnosis'][row]]
#
#     return data


def gender_encoding(data):
    for row in range(data.shape[0]):
        if data["Gender"][row] == "Male":
            data.loc[row, "Gender"] = 0
        else:
            data.loc[row, "Gender"] = 1
    return data


def country_encoding(data):
    countries = ['Russia', 'Germany', 'Nigeria', 'India', 'UK', 'South Korea', 'Brazil', 'China', 'Japan', 'USA']

    # Create a mapping from country name to its index
    country_to_index = {country: index for index, country in enumerate(countries)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Country'] = country_to_index[data['Country'][row]]

    return data

def ethnicity_encoding(data):
    ethnicities = ['Caucasian', 'Hispanic', 'Asian', 'African', 'Middle Eastern']

    # Create a mapping from country name to its index
    ethnicity_to_index = {ethnicity: index for index, ethnicity in enumerate(ethnicities)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Ethnicity'] = ethnicity_to_index[data['Ethnicity'][row]]

    return data

def family_history_encoding(data):
    FHs = ['Yes', 'No']

    # Create a mapping from country name to its index
    FH_to_index = {FH: index for index, FH in enumerate(FHs)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Family_History'] = FH_to_index[data['Family_History'][row]]

    return data

def radiation_exposure_encoding(data):
    radiation_exposures = ['Yes', 'No']

    # Create a mapping from country name to its index
    radiation_exposure_to_index = {radiation_exposure: index for index, radiation_exposure in enumerate(radiation_exposures)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Radiation_Exposure'] = radiation_exposure_to_index[data['Radiation_Exposure'][row]]

    return data

def iodine_deficiency_encoding(data):
    iodine_deficiencies = ['Yes', 'No']

    # Create a mapping from country name to its index
    iodine_deficiency_to_index = {iodine_deficiency: index for index, iodine_deficiency in enumerate(iodine_deficiencies)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Iodine_Deficiency'] = iodine_deficiency_to_index[data['Iodine_Deficiency'][row]]

    return data


def smoking_encoding(data):
    smoking_encodings = ['Yes', 'No']

    # Create a mapping from country name to its index
    smoking_to_index = {smoking_encoding: index for index, smoking_encoding in enumerate(smoking_encodings)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Smoking'] = smoking_to_index[data['Smoking'][row]]

    return data


def obesity_encoding(data):
    obesity_encodings = ['Yes', 'No']

    # Create a mapping from country name to its index
    obesity_to_index = {obesity_encoding: index for index, obesity_encoding in enumerate(obesity_encodings)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Obesity'] = obesity_to_index[data['Obesity'][row]]

    return data


def diabetes_encoding(data):
    diabetes_encodings = ['Yes', 'No']

    # Create a mapping from country name to its index
    diabetes_to_index = {diabetes_encoding: index for index, diabetes_encoding in enumerate(diabetes_encodings)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Diabetes'] = diabetes_to_index[data['Diabetes'][row]]

    return data


def thyroid_cancer_risk_encoding(data):
    thyroid_cancer_risk_encodings = ['Low', 'Medium', 'High']

    # Create a mapping from country name to its index
    thyroid_cancer_risk_to_index = {thyroid_cancer_risk_encoding: index for index, thyroid_cancer_risk_encoding in enumerate(thyroid_cancer_risk_encodings)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Thyroid_Cancer_Risk'] = thyroid_cancer_risk_to_index[data['Thyroid_Cancer_Risk'][row]]

    return data


def diagnosis_encoding(data):
    diagnosis_encodings = ['Benign', 'Malignant']

    # Create a mapping from country name to its index
    diagnosis_to_index = {diagnosis_encoding: index for index, diagnosis_encoding in enumerate(diagnosis_encodings)}

    # Replace the 'country' column values with their corresponding indices
    for row in range(data.shape[0]):
        data.loc[row, 'Diagnosis'] = diagnosis_to_index[data['Diagnosis'][row]]

    return data


def process_data_thru_pipeline(data):
    if data.empty:
        raise IndexError
    data = pt_identifier_removal(data)
#   data = encoder(data)
    data = gender_encoding(data)
    data = country_encoding(data)
    data = ethnicity_encoding(data)
    data = family_history_encoding(data)
    data = radiation_exposure_encoding(data)
    data = iodine_deficiency_encoding(data)
    data = smoking_encoding(data)
    data = obesity_encoding(data)
    data = diabetes_encoding(data)
    data = thyroid_cancer_risk_encoding(data)
    data = diagnosis_encoding(data)
    return data


def identify_outliers(df, columns):
    """
    Identify outliers in specified columns of a DataFrame using the IQR method.

    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.
    columns (list): List of column names to check for outliers.

    Returns:
    dict: A dictionary where keys are column names and values are DataFrames containing the outliers for each column.
    """
    outliers_dict = {}

    for col in columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            outliers_dict[col] = outliers

    return outliers_dict