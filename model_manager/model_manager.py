# from pytorch_tabnet.tab_network import TabNet
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, \
    ExtraTreesClassifier
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import (classification_report, accuracy_score, confusion_matrix, mean_squared_error,
#                              mean_absolute_error, make_scorer)
from sklearn.metrics import accuracy_score
# from sklearn.pipeline import Pipeline
# from skorch import NeuralNetClassifier
# from tab_transformer_pytorch import TabTransformer, FTTransformer
# from tsai.models.GatedTabTransformer import GatedTabTransformer
# from pytorch_tabular import TabularModel
from pytorch_tabular.config import DataConfig, ModelConfig, TrainerConfig
import warnings
#import torch


warnings.filterwarnings('ignore')


def init_basic_models():
    # categorical_classes = ['Thyroid_Cancer_Risk', 'Gender_Male',
    #        'Country_China', 'Country_Germany', 'Country_India', 'Country_Japan', 'Country_Nigeria', 'Country_Russia',
    #        'Country_South Korea', 'Country_UK', 'Country_USA', 'Ethnicity_Asian', 'Ethnicity_Caucasian',
    #        'Ethnicity_Hispanic', 'Ethnicity_Middle Eastern', 'Family_History_Yes', 'Radiation_Exposure_Yes',
    #        'Iodine_Deficiency_Yes', 'Smoking_Yes', 'Obesity_Yes', 'Diabetes_Yes']
    # continuous_classes = ['Age', 'TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size']
    # c_out = 1
    # tuple_categorical_classes = (3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    # num_continuous = 5
    # target_class = ['Diagnosis_Malignant']
    #
    # data_config = DataConfig(
    #     target=target_class,
    #     continuous_cols=continuous_classes,
    #     categorical_cols=categorical_classes,
    # )
    #
    # model_config = ModelConfig(
    #     task='classification',
    #     _model_name='tabnet'
    # )
    #
    # trainer_config = TrainerConfig(
    #     max_epochs=10,
    # )
    #
    # transformer = TabTransformer(
    #     categories=tuple_categorical_classes,
    #     num_continuous=num_continuous,
    #     dim=32,
    #     depth=6,
    #     heads=8,
    #     ff_dropout=0.1
    # )
    #
    # net = NeuralNetClassifier(
    #     module=transformer,
    #     optimizer=torch.optim.Adam,
    #     lr=0.001,
    #     max_epochs=10,
    #     iterator_train__shuffle=True,
    #     device='cuda' if torch.cuda.is_available() else 'cpu'
    # )
    #
    # pipeline = Pipeline([(
    #     'Tab_Transformer', net
    # )])

    return {
        'Logistic_Regression': LogisticRegression(random_state=42),
        'KNeighbors_Classifier': KNeighborsClassifier(),
        'Support_Vector_Machine': SVC(random_state=42),
        'Decision_Tree_Classifier': DecisionTreeClassifier(random_state=42),
        'Random_Forest_Classifier': RandomForestClassifier(random_state=42),
        'AdaBoost_Classifier': AdaBoostClassifier(random_state=42),
        'Gradient_Boosting_Classifier': GradientBoostingClassifier(random_state=42),
        'Extra_Trees_Classifier': ExtraTreesClassifier(random_state=42),
        'XGBoost_Classifier': XGBClassifier(random_state=42),
        'GaussianNB_Classifier': GaussianNB()
    }
        #'Tab_Transformer': pipeline,
    # ('Gated_Tab_Transformer', GatedTabTransformer(
    #     classes = categorical_classes,
    #     cont_names = continuous_classes,
    #     c_out = c_out,
    #     column_embed = True,
    #     add_shared_embed = False,
    #     shared_embed_div = 8,
    #     drop_whole_embed=False,
    #     d_model=32,
    #     n_layers=6,
    #     n_heads=8,
    #     d_k=None,
    #     d_v=None,
    #     d_ff=None,
    #     res_attention=True,
    #     attention_act='gelu',
    #     res_dropout=0.1,
    #     norm_cont=True,
    #     mlp_d_model=32,
    #     mlp_d_ffn=64,
    #     mlp_layers=4
    #     )
    # ),
    #     'FT_Transformer', FTTransformer(
    #         categories=tuple_categorical_classes,
    #         num_continuous=num_continuous,
    #         dim=32,
    #         depth=6,
    #         heads=8,
    #         ff_dropout=0.1,
    #         ),
    # ('Tab_Net', TabularModel(
    #     data_config=data_config,
    #     model_config=model_config,
    #     trainer_config=trainer_config
    #     )
    # )



def split_data(input, output):
    return train_test_split(input, output, test_size=0.2, random_state=42)


#def get_cross_val_score(model, inputs, outputs, categorical_tensor, continuous_tensor):
def get_cross_val_score(model, inputs, outputs):
    #scorer = make_scorer(accuracy_score)
    #return cross_val_score(model, categorical_tensor, continuous_tensor, cv=5, scoring=scorer).mean()
    return cross_val_score(model, inputs, outputs, cv=5).mean()


#def train_models(models, inputs, output, categorical_tensor, continuous_tensor):
def train_models(models, inputs, output):
    scores = {}
    for model_name in models:
        #scores[model_name] = get_cross_val_score(models[model_name], inputs, output, categorical_tensor, continuous_tensor)
        scores[model_name] = get_cross_val_score(models[model_name], inputs, output)
        models[model_name].fit(inputs, output)
    return models, scores


def get_accuracy(model, inputs, outputs):
    return accuracy_score(outputs, model.predict(inputs))

def get_accuracy_scores(models, inputs, outputs):
    scores = {}
    for model_name in models:
        scores[model_name] = get_accuracy(models[model_name], inputs, outputs)
    return scores


def run_models(inputs, outputs):
    models = init_basic_models()
    #models = {'Tab_Transformer': models['Tab_Transformer']}
    input_train, input_test, output_train, output_test = split_data(inputs, outputs)
    #models = {'Logistic_Regression': models['Logistic_Regression']}
    #categorical_classes = ['Thyroid_Cancer_Risk', 'Gender_Male',
    #                        'Country_China', 'Country_Germany', 'Country_India', 'Country_Japan', 'Country_Nigeria',
    #                        'Country_Russia',
    #                        'Country_South Korea', 'Country_UK', 'Country_USA', 'Ethnicity_Asian', 'Ethnicity_Caucasian',
    #                        'Ethnicity_Hispanic', 'Ethnicity_Middle Eastern', 'Family_History_Yes',
    #                        'Radiation_Exposure_Yes',
    #                        'Iodine_Deficiency_Yes', 'Smoking_Yes', 'Obesity_Yes', 'Diabetes_Yes']
    # continuous_classes = ['Age', 'TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size']
    # categorical_data = input_train[categorical_classes]
    # continuous_data = input_train[continuous_classes]
    # categorical_tensor = torch.tensor(categorical_data.values)
    # continuous_tensor = torch.tensor(continuous_data.values)
    #models, cross_val_scores = train_models(models, input_train, output_train, categorical_tensor, continuous_tensor)
    models, cross_val_scores = train_models(models, input_train, output_train)
    accuracy_scores = get_accuracy_scores(models, input_test, output_test)
    return cross_val_scores, accuracy_scores

