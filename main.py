# My name is Rajesh Kumar Butta, and this is my work.
# 2/8/25

import data_processor as dp
import data_visualizer as dv
import pandas as pd
import time

file_path = "thyroid_cancer_risk/thyroid_cancer_risk_data.csv"
processed_data_file_path = 'thyroid_cancer_risk/processed_data.parquet'


def get_data(file_path):
    unprocessed_thyroid_data = dp.get_all_data(file_path)
    return unprocessed_thyroid_data


def process_data(unprocessed_thyroid_data):
    processed_data = dp.process_data_thru_pipeline(unprocessed_thyroid_data)
    processed_data.to_parquet("thyroid_cancer_risk/processed_data.parquet", engine="pyarrow", compression="snappy")


def run(file_path, processed_data_file_path):
    unprocessed_thyroid_data = get_data(file_path)
    processed_data = pd.read_parquet(processed_data_file_path)
    dv.create_plots(processed_data, unprocessed_thyroid_data)
    dv.outlier_analysis(unprocessed_thyroid_data)
    dp.identify_outliers(unprocessed_thyroid_data, ['Age', 'TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size'])


if __name__ == "__main__":
    run(file_path, processed_data_file_path)