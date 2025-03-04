import unittest
import data_processor.data_processor as dp
import model_manager.model_manager as mm
import pandas as pd

class TestCase(unittest.TestCase):
    filepath = "thyroid_cancer_risk/thyroid_cancer_risk_data.csv"
    data = dp.get_all_data(filepath)
    data_slice = data[0:1]
    empty_data = pd.DataFrame()

    def test_get_all_data(self):
        self.assertIsNotNone(dp.get_all_data(self.filepath))
        self.assertRaises(FileNotFoundError, dp.get_all_data, "wrong_path")

    def test_pipeline(self):
        new_data = self.data
        new_empty_data = self.empty_data
        #self.assertIsNotNone(dp.process_data_thru_pipeline(new_data))
        self.assertRaises(IndexError, dp.process_data_thru_pipeline, new_empty_data)

    def test_identifier_removal(self):
        new_data = self.data
        self.assertEqual(new_data.shape[1]-1, dp.pt_identifier_removal(new_data).shape[1])

    def test_gender_encoder(self):
        new_data = self.data
        self.assertEqual(isinstance(dp.gender_encoding(new_data[0:1])["Gender_Male"][0], int), True)

    def test_country_encoder(self):
        self.assertEqual(isinstance(dp.country_encoding(self.data_slice)["Country"][0], int), True)

    def test_ethnicity_encoder(self):
        self.assertEqual(isinstance(dp.ethnicity_encoding(self.data_slice)["Ethnicity"][0], int), True)

    def test_Family_History_encoder(self):
        self.assertEqual(isinstance(dp.family_history_encoding(self.data_slice)["Family_History_Yes"][0], int), True)

    def test_radiation_exposure_encoder(self):
        self.assertEqual(isinstance(dp.radiation_exposure_encoding(self.data_slice)["Radiation_Exposure_Yes"][0], int), True)

    def test_iodine_deficiency_encoder(self):
        self.assertEqual(isinstance(dp.iodine_deficiency_encoding(self.data_slice)["Iodine_Deficiency_Yes"][0], int), True)

    def test_smoking_encoder(self):
        self.assertEqual(isinstance(dp.smoking_encoding(self.data_slice)["Smoking_Yes"][0], int), True)

    def test_obesity_encoder(self):
        self.assertEqual(isinstance(dp.obesity_encoding(self.data_slice)["Obesity_Yes"][0], int), True)

    def test_diabetes_encoder(self):
        self.assertEqual(isinstance(dp.diabetes_encoding(self.data_slice)["Diabetes_Yes"][0], int), True)

    def test_thyroid_cancer_risk_encoder(self):
        self.assertEqual(isinstance(dp.thyroid_cancer_risk_encoding(self.data_slice)["Thyroid_Cancer_Risk"][0], int), True)

    def test_diagnosis_encoder(self):
        self.assertEqual(isinstance(dp.diagnosis_encoding(self.data_slice)["Diagnosis_Malignant"][0], int), True)

    def test_model_creation(self):
        self.assertEqual(len(mm.init_models()), 11)