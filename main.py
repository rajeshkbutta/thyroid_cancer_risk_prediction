# My name is Rajesh Kumar Butta, and this is my work.
# 2/8/25

import data_processor as dp
import data_visualizer as dv
import pandas as pd
import time
import model_manager as mm
import logging as log

file_path = "thyroid_cancer_risk/thyroid_cancer_risk_data.csv"
processed_data_file_path = 'thyroid_cancer_risk/processed_data.parquet'


def get_data(file_path):
    try:
        unprocessed_thyroid_data = dp.get_all_data(file_path)
        log.log(level=log.DEBUG, msg="Processing data")
        return unprocessed_thyroid_data
    except FileNotFoundError as e:
        log.log(level=log.ERROR, msg="File error")


def process_data(unprocessed_thyroid_data):
    processed_data = dp.process_data_thru_pipeline(unprocessed_thyroid_data)
    processed_data.to_parquet("thyroid_cancer_risk/processed_data.parquet", engine="pyarrow", compression="snappy")


def run(file_path, processed_data_file_path):
    unprocessed_thyroid_data = get_data(file_path)
    #processed_data = dp.process_data_thru_pipeline(unprocessed_thyroid_data)
    #processed_data.to_parquet(processed_data_file_path, engine="pyarrow", compression="snappy")
    processed_data = pd.read_parquet(processed_data_file_path)
    #dv.create_plots(processed_data, unprocessed_thyroid_data)
    #dv.outlier_analysis(unprocessed_thyroid_data)
    #outlier = dp.identify_outliers(unprocessed_thyroid_data, ['Age', 'TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size'])
    inputs, outputs = dp.input_output_split(processed_data)
    normalized_inputs = dp.normalize_all_data(inputs)
    cross_val_scores, accuracy_scores = mm.run_models(normalized_inputs, outputs)
    dv.plot_model_comparison(cross_val_scores)
    dv.plot_model_comparison(accuracy_scores)
    print("Cross validation scores:", cross_val_scores)
    print("Accuracy scores:", accuracy_scores)



if __name__ == "__main__":
    log.log(level=log.DEBUG, msg="Starting...")
    run(file_path, processed_data_file_path)