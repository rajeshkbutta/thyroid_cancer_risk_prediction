import pandas as pd
import category_encoders as ce
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder


one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first')


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
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Gender']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Gender'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Gender', axis=1), encoded_df], axis=1)

    return df_encoded


def country_encoding(data):
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Country']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Country'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Country', axis=1), encoded_df], axis=1)

    return df_encoded


def ethnicity_encoding(data):
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Ethnicity']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Ethnicity'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Ethnicity', axis=1), encoded_df], axis=1)

    return df_encoded


def family_history_encoding(data):
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Family_History']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Family_History'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Family_History', axis=1), encoded_df], axis=1)

    return df_encoded


def radiation_exposure_encoding(data):
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Radiation_Exposure']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Radiation_Exposure'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Radiation_Exposure', axis=1), encoded_df], axis=1)

    return df_encoded


def iodine_deficiency_encoding(data):
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Iodine_Deficiency']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Iodine_Deficiency'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Iodine_Deficiency', axis=1), encoded_df], axis=1)

    return df_encoded


def smoking_encoding(data):
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Smoking']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Smoking'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Smoking', axis=1), encoded_df], axis=1)

    return df_encoded


def obesity_encoding(data):
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Obesity']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Obesity'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Obesity', axis=1), encoded_df], axis=1)

    return df_encoded


def diabetes_encoding(data):
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Diabetes']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Diabetes'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Diabetes', axis=1), encoded_df], axis=1)

    return df_encoded


def thyroid_cancer_risk_encoding(data):
    order = ['Low','Medium','High']
    ordinal_encoder = OrdinalEncoder(categories=[order])
    data[['Thyroid_Cancer_Risk']] = ordinal_encoder.fit_transform(data[['Thyroid_Cancer_Risk']])
    return data


def diagnosis_encoding(data):
    global one_hot_encoder
    encoded_data = one_hot_encoder.fit_transform(data[['Diagnosis']])
    # Get feature names
    encoded_columns = one_hot_encoder.get_feature_names_out(['Diagnosis'])

    # Create a DataFrame with encoded features
    encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

    # Concatenate with the original DataFrame (excluding original categorical columns)
    df_encoded = pd.concat([data.drop('Diagnosis', axis=1), encoded_df], axis=1)

    return df_encoded


def input_output_split(df):
    input = df.drop(['Diagnosis_Malignant'], axis=1)
    output = df['Diagnosis_Malignant']
    return input, output


def process_data_thru_pipeline(data):
    if data.empty:
        raise IndexError
    data = pt_identifier_removal(data)
    #data = encoder(data)
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


def data_normalization(data):
    return (data-data.mean())/data.std()


def normalize_all_data(df):
    normalizable_columns = ['Age', 'TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size']
    for col in normalizable_columns:
        df[col] = data_normalization(df[col])
    return df