import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch


def plot_age_histogram(df):
    # Check if 'age' column exists
    if 'Age' not in df.columns:
        print("The dataframe does not have an 'age' column.")
        return

    # Get the 'age' column from the dataframe
    age = df['Age']

    # Calculate mean, median, and standard deviation
    mean_age = np.mean(age)
    median_age = np.median(age)
    std_age = np.std(age)

    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(age, bins=20, edgecolor='black', alpha=0.7, color='blue')

    # Add vertical lines for mean, median, and standard deviation
    plt.axvline(mean_age, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_age:.2f}')
    plt.axvline(median_age, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_age:.2f}')
    plt.axvline(mean_age + std_age, color='orange', linestyle='dashed', linewidth=2,
                label=f'Mean + 1 Std Dev: {mean_age + std_age:.2f}')
    plt.axvline(mean_age - std_age, color='orange', linestyle='dashed', linewidth=2,
                label=f'Mean - 1 Std Dev: {mean_age - std_age:.2f}')

    # Labels and title
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')

    # Show the legend
    plt.legend()

    # Show the plot
    plt.show()

    # Print the mean, median, and standard deviation
    print(f"Mean age: {mean_age:.2f}")
    print(f"Median age: {median_age:.2f}")
    print(f"Standard deviation of age: {std_age:.2f}")


def plot_age_gender_distribution(df):
    """
    Plots the age distribution for each gender and displays statistical measures.

    Parameters:
    df (pandas.DataFrame): DataFrame containing 'age' and 'gender' columns.

    Returns:
    None
    """
    # Check if 'age' and 'gender' columns exist
    if 'Age' not in df.columns or 'Gender' not in df.columns:
        print("The dataframe must contain 'age' and 'gender' columns.")
        return

    # Drop rows with missing values in 'age' or 'gender'
    df = df.dropna(subset=['Age', 'Gender'])

    # Separate data by gender
    males = df[df['Gender'] == 0]['Age']
    females = df[df['Gender'] == 1]['Age']

    # Calculate statistics
    stats = {}
    for group, label in zip([males, females], ['Male', 'Female']):
        stats[label] = {
            'mean': np.mean(group),
            'median': np.median(group),
            'std': np.std(group)
        }

    # Plot histograms
    plt.figure(figsize=(12, 6))
    plt.hist(males, bins=20, alpha=0.5, label='Male', color='blue', edgecolor='black')
    plt.hist(females, bins=20, alpha=0.5, label='Female', color='pink', edgecolor='black')

    # Add vertical lines for mean
    plt.axvline(stats['Male']['mean'], color='blue', linestyle='dashed', linewidth=2)
    plt.axvline(stats['Female']['mean'], color='pink', linestyle='dashed', linewidth=2)

    # Add labels and title
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age Distribution by Gender')
    plt.legend()

    # Show plot
    plt.show()

    # Print statistics
    for gender, stat in stats.items():
        print(f"{gender} - Mean age: {stat['mean']:.2f}, Median age: {stat['median']:.2f}, "
              f"Standard deviation: {stat['std']:.2f}")

# Example usage:
# Assuming 'df' is your DataFrame containing 'age' and 'gender' columns
# plot_age_gender_distribution(df)


def plot_country_distribution(df):
    """
    Plots the distribution of countries in the 'Countries' column of the given DataFrame.

    Parameters:
    df (pandas.DataFrame): DataFrame containing a 'Countries' column.

    Returns:
    None
    """
    # Check if 'Countries' column exists
    if 'Country' not in df.columns:
        print("The DataFrame does not have a 'Country' column.")
        return

    # Drop rows with missing values in 'Countries' column
    df = df.dropna(subset=['Country'])

    # Define the list of countries to include in the plot
    countries = ['Russia', 'Germany', 'Nigeria', 'India', 'UK', 'South Korea', 'Brazil', 'China', 'Japan', 'USA']

    # Filter the DataFrame to include only the specified countries
    df_filtered = df[df['Country'].isin(countries)]

    # Count the occurrences of each country
    country_counts = df_filtered['Country'].value_counts().reindex(countries, fill_value=0)

    # Plotting
    plt.figure(figsize=(12, 6))
    country_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Country Distribution')
    plt.xlabel('Country')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Show the plot
    plt.show()

# Example usage:
# Assuming 'df' is your DataFrame containing a 'Countries' column
# plot_country_distribution(df)


import matplotlib.pyplot as plt
import pandas as pd

def plot_age_distribution_by_country(df):
    """
    Plots the age distribution for each country in the 'Countries' column of the given DataFrame.

    Parameters:
    df (pandas.DataFrame): DataFrame containing 'Age' and 'Countries' columns.

    Returns:
    None
    """
    # Check if 'Age' and 'Countries' columns exist
    if 'Age' not in df.columns or 'Country' not in df.columns:
        print("The DataFrame must contain 'Age' and 'Country' columns.")
        return

    # Drop rows with missing values in 'Age' or 'Countries'
    df = df.dropna(subset=['Age', 'Country'])

    # Get the list of unique countries
    countries = df['Country'].unique()

    # Determine the number of rows and columns for subplots
    num_countries = len(countries)
    num_cols = 3
    num_rows = (num_countries + num_cols - 1) // num_cols  # Ceiling division

    # Create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, num_rows * 5), sharex=True, sharey=True)
    axes = axes.flatten()  # Flatten in case of multiple rows

    # Plot each country's age distribution
    for i, country in enumerate(countries):
        country_data = df[df['Country'] == country]['Age']
        axes[i].hist(country_data, bins=20, edgecolor='black', alpha=0.7)
        axes[i].set_title(f'Age Distribution in {country}')
        axes[i].set_xlabel('Age')
        axes[i].set_ylabel('Frequency')

    # Remove any unused subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout
    plt.tight_layout()
    plt.show()

# Example usage:
# Assuming 'df' is your DataFrame containing 'Age' and 'Countries' columns
# plot_age_distribution_by_country(df)


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_population_pyramids(df):
    """
    Plots population pyramids (age distribution by gender) for each country in the DataFrame.

    Parameters:
    df (pandas.DataFrame): DataFrame containing 'Age', 'Gender', and 'Country' columns.

    Returns:
    None
    """
    # Check if required columns exist
    if not {'Age', 'Gender', 'Country'}.issubset(df.columns):
        print("The DataFrame must contain 'Age', 'Gender', and 'Country' columns.")
        return

    # Drop rows with missing values in 'Age', 'Gender', or 'Country'
    df = df.dropna(subset=['Age', 'Gender', 'Country'])

    # Define the list of countries to include in the plot
    countries = ['Russia', 'Germany', 'Nigeria', 'India', 'UK', 'South Korea', 'Brazil', 'China', 'Japan', 'USA']

    # Filter the DataFrame to include only the specified countries
    df_filtered = df[df['Country'].isin(countries)]

    # Define age bins and labels
    age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    age_labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90+']
    df_filtered['AgeGroup'] = pd.cut(df_filtered['Age'], bins=age_bins, labels=age_labels, right=False)

    # Determine the number of rows and columns for subplots
    num_countries = len(countries)
    num_cols = 2
    num_rows = (num_countries + num_cols - 1) // num_cols  # Ceiling division

    # Create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, num_rows * 5), sharex=True)

    # Flatten axes array for easy iteration
    axes = axes.flatten()

    # Plot population pyramid for each country
    for idx, country in enumerate(countries):
        ax = axes[idx]
        country_data = df_filtered[df_filtered['Country'] == country]

        # Calculate the population counts for each age group and gender
        population_data = country_data.groupby(['AgeGroup', 'Gender']).size().unstack(fill_value=0)

        # Ensure both Male and Female columns exist
        if 'Male' not in population_data.columns:
            population_data['Male'] = 0
        if 'Female' not in population_data.columns:
            population_data['Female'] = 0

        # Plot male population (negative values for left side)
        ax.barh(population_data.index, -population_data['Male'], color='blue', label='Male')
        # Plot female population
        ax.barh(population_data.index, population_data['Female'], color='pink', label='Female')

        # Set titles and labels
        ax.set_title(country)
        ax.set_xlabel('Population')
        ax.set_ylabel('Age Group')
        ax.legend()

    # Remove any unused subplots
    for j in range(idx + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout
    plt.tight_layout()
    plt.show()

# Example usage:
# Assuming 'df' is your DataFrame containing 'Age', 'Gender', and 'Country' columns
# plot_population_pyramids(df)


def plot_age_distribution_by_ethnicity(df):
    """
    Plots histograms of age distribution for each ethnicity in the DataFrame.

    Parameters:
    df (pandas.DataFrame): DataFrame containing 'Ethnicity' and 'Age' columns.

    Returns:
    None
    """
    # Define the order of ethnicities for consistent plotting
    ethnicity_order = ['Caucasian', 'Hispanic', 'Asian', 'African', 'Middle Eastern']

    # Set the aesthetic style of the plots
    sns.set_style("whitegrid")

    # Create a figure and axes
    plt.figure(figsize=(12, 8))

    # Plot histograms for each ethnicity
    for ethnicity in ethnicity_order:
        subset = df[df['Ethnicity'] == ethnicity]
        sns.histplot(subset['Age'], kde=True, label=ethnicity, bins=10, alpha=0.5)

    # Add titles and labels
    plt.title('Age Distribution by Ethnicity')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.legend(title='Ethnicity')
    plt.show()


def plot_ethnicity_gender_histogram(df):
    """
    Create a grouped histogram for Ethnicity and Gender in a single plot

    Parameters:
    df (pandas.DataFrame): DataFrame containing 'Ethnicity' and 'Gender' columns
    """
    # Create crosstab of Ethnicity and Gender
    crosstab = pd.crosstab(df['Ethnicity'], df['Gender'])

    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Parameters for bars
    n_groups = len(crosstab.index)
    bar_width = 0.35
    index = np.arange(n_groups)

    # Plot bars
    for i, gender in enumerate(crosstab.columns):
        plt.bar(index + i * bar_width,
                crosstab[gender],
                bar_width,
                label=gender,
                alpha=0.8)

    # Customize the plot
    plt.xlabel('Ethnicity')
    plt.ylabel('Count')
    plt.title('Distribution of Ethnicity and Gender')
    plt.xticks(index + bar_width / 2, crosstab.index, rotation=45)
    plt.legend(title='Gender')
    plt.tight_layout()

    # Display the plot
    plt.show()


def plot_ethnicity_distribution_by_country(df):
    """
    Plots a stacked bar chart of ethnicity distribution for each country in the DataFrame.

    Parameters:
    df (pandas.DataFrame): DataFrame containing 'Ethnicity' and 'Country' columns.

    Returns:
    None
    """
    # Set the aesthetic style of the plots
    sns.set_style("whitegrid")

    # Create a pivot table to count occurrences of each combination
    pivot_table = pd.pivot_table(df, index='Country', columns='Ethnicity', aggfunc='size', fill_value=0)

    # Plot the stacked bar chart
    pivot_table.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='Set2')

    # Add titles and labels
    plt.title('Ethnicity Distribution by Country')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_family_history_relationships(df):
    """
    Plots histograms of specified features grouped by Family_History.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Define the features to plot
    features = ['Age', 'Gender', 'Country', 'Ethnicity']

    # Set the style of the plots
    sns.set(style="whitegrid")

    palette = {'Yes': 'C0', 'No': 'C1'}

    # Create a figure with subplots
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
    axes = axes.flatten()

    # Iterate over the features and create a histogram for each
    for i, feature in enumerate(features):
        sns.histplot(data=df, x=feature, hue='Family_History', multiple='stack', palette='Set2', ax=axes[i])
        axes[i].set_title(f'Distribution of {feature} by Family History')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Count')

        # Create custom legend
        legend_labels = {'Yes': 'Family History: Yes', 'No': 'Family History: No'}
        handles = [Patch(color=palette[key], label=legend_labels[key]) for key in legend_labels]
        fig.legend(handles=handles, title='Family History', loc='upper right')

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_radiation_exposure_relationships(df):
    """
    Plots bar plots of specified features grouped by Radiation_Exposure.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Define the features to plot
    features = ['Age', 'Gender', 'Country', 'Ethnicity', 'Family_History']

    # Set the style of the plots
    sns.set(style="whitegrid")

    # Create a figure with subplots
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))
    axes = axes.flatten()

    # Define colors for 'Yes' and 'No' categories
    palette = {'Yes': 'C0', 'No': 'C1'}

    # Iterate over the features and create a bar plot for each
    for i, feature in enumerate(features):
        if feature == 'Age':
            # For continuous variable 'Age', use histplot
            sns.histplot(data=df, x=feature, hue='Radiation_Exposure', multiple='stack', palette=palette, ax=axes[i],
                         bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='Radiation_Exposure', palette=palette, ax=axes[i])

        axes[i].set_title(f'Distribution of {feature} by Radiation Exposure')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Count')

    # Remove the last subplot if the number of features is odd
    if len(features) % 2 != 0:
        fig.delaxes(axes[-1])

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_iodine_deficiency_relationships(df):
    """
    Plots bar plots of specified features grouped by Iodine_Deficiency.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Define the features to plot
    features = ['Age', 'Gender', 'Country', 'Ethnicity', 'Family_History', 'Radiation_Exposure']

    # Set the style of the plots
    sns.set(style="whitegrid")

    # Create a figure with subplots
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))
    axes = axes.flatten()

    # Define colors for 'Yes' and 'No' categories
    palette = {'Yes': 'C0', 'No': 'C1'}

    # Iterate over the features and create a bar plot for each
    for i, feature in enumerate(features):
        if feature == 'Age':
            # For continuous variable 'Age', use histplot
            sns.histplot(data=df, x=feature, hue='Iodine_Deficiency', multiple='stack', palette=palette, ax=axes[i],
                         bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='Iodine_Deficiency', palette=palette, ax=axes[i])

        axes[i].set_title(f'Distribution of {feature} by Iodine Deficiency')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Count')

    # Remove the last subplot if the number of features is odd
    if len(features) % 2 != 0:
        fig.delaxes(axes[-1])

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_smoking_relationships(df):
    """
    Plots bar plots of specified features grouped by Smoking status.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Define the features to plot
    features = ['Age', 'Gender', 'Country', 'Ethnicity', 'Family_History', 'Radiation_Exposure', 'Iodine_Deficiency']

    # Set the style of the plots
    sns.set(style="whitegrid")

    # Create a figure with subplots
    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(15, 20))
    axes = axes.flatten()

    # Define colors for 'Yes' and 'No' categories
    palette = {'Yes': 'C0', 'No': 'C1'}

    # Iterate over the features and create a bar plot for each
    for i, feature in enumerate(features):
        if feature == 'Age':
            # For continuous variable 'Age', use histplot
            sns.histplot(data=df, x=feature, hue='Smoking', multiple='stack', palette=palette, ax=axes[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='Smoking', palette=palette, ax=axes[i])

        axes[i].set_title(f'Distribution of {feature} by Smoking Status')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Count')

    # Remove the last subplot if the number of features is odd
    if len(features) % 2 != 0:
        fig.delaxes(axes[-1])

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_obesity_relationships(df):
    """
    Plots bar plots of specified features grouped by Obesity status.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Define the features to plot
    features = ['Age', 'Gender', 'Country', 'Ethnicity', 'Family_History', 'Radiation_Exposure', 'Iodine_Deficiency',
                'Smoking']

    # Set the style of the plots
    sns.set(style="whitegrid")

    # Create a figure with subplots
    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(15, 20))
    axes = axes.flatten()

    # Define colors for 'Yes' and 'No' categories
    palette = {'Yes': 'C0', 'No': 'C1'}

    # Iterate over the features and create a bar plot for each
    for i, feature in enumerate(features):
        if feature == 'Age':
            # For continuous variable 'Age', use histplot
            sns.histplot(data=df, x=feature, hue='Obesity', multiple='stack', palette=palette, ax=axes[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='Obesity', palette=palette, ax=axes[i])

        axes[i].set_title(f'Distribution of {feature} by Obesity Status')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Count')

    # Remove the last subplot if the number of features is odd
    if len(features) % 2 != 0:
        fig.delaxes(axes[-1])

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_diabetes_relationships(df):
    """
    Plots histograms of specified features grouped by Diabetes status.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Define the features for the first plot
    features_first_plot = ['Age', 'Gender', 'Country', 'Ethnicity']

    # Define the features for the second plot
    features_second_plot = ['Family_History', 'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking', 'Obesity']

    # Set the style of the plots
    sns.set(style="whitegrid")

    # Create the first figure with subplots
    fig1, axes1 = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
    axes1 = axes1.flatten()

    # Plot the first set of features
    for i, feature in enumerate(features_first_plot):
        if feature == 'Age':
            # For continuous variable 'Age', use histplot
            sns.histplot(data=df, x=feature, hue='Diabetes', multiple='stack', ax=axes1[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='Diabetes', ax=axes1[i])

        axes1[i].set_title(f'Distribution of {feature} by Diabetes Status')
        axes1[i].set_xlabel(feature)
        axes1[i].set_ylabel('Count')

    # Adjust layout for the first plot
    plt.tight_layout()
    plt.show()

    # Create the second figure with subplots
    fig2, axes2 = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))
    axes2 = axes2.flatten()

    # Plot the second set of features
    for i, feature in enumerate(features_second_plot):
        if feature == 'Age':
            # For continuous variable 'Age', use histplot
            sns.histplot(data=df, x=feature, hue='Diabetes', multiple='stack', ax=axes2[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='Diabetes', ax=axes2[i])

        axes2[i].set_title(f'Distribution of {feature} by Diabetes Status')
        axes2[i].set_xlabel(feature)
        axes2[i].set_ylabel('Count')

    if len(features_second_plot) % 2 != 0:
        fig2.delaxes(axes2[-1])

    # Adjust layout for the second plot
    plt.tight_layout()
    plt.show()


def plot_tsh_binned_relationships(df):
    """
    Plots histograms of specified features, grouped by binned TSH_Level.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Create bins for TSH_Level
    bins = [0, 2.5, 5.0, 7.5, 10]  # Binning the TSH_Level into 4 categories
    labels = ['Low', 'Normal', 'High', 'Very High']
    df['TSH_Level_binned'] = pd.cut(df['TSH_Level'], bins=bins, labels=labels, right=False)

    # Define the features for the first plot
    features_first_plot = ['Age', 'Gender', 'Country', 'Ethnicity', 'Diabetes']

    # Define the features for the second plot
    features_second_plot = ['Family_History', 'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking', 'Obesity']

    # Set the style of the plots
    sns.set(style="whitegrid")

    # Create the first figure with subplots
    fig1, axes1 = plt.subplots(nrows=3, ncols=2, figsize=(15, 10))
    axes1 = axes1.flatten()

    # Plot the first set of features
    for i, feature in enumerate(features_first_plot):
        if feature == 'Age':
            # For continuous variable 'Age', use histplot
            sns.histplot(data=df, x=feature, hue='TSH_Level_binned', multiple='stack', ax=axes1[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='TSH_Level_binned', ax=axes1[i])

        axes1[i].set_title(f'Distribution of {feature} by TSH_Level')
        axes1[i].set_xlabel(feature)
        axes1[i].set_ylabel('Count')

    if len(features_second_plot) % 2 != 0:
        fig1.delaxes(axes1[-1])

    # Adjust layout for the first plot
    plt.tight_layout()
    plt.show()

    # Create the second figure with subplots
    fig2, axes2 = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))
    axes2 = axes2.flatten()

    # Plot the second set of features
    for i, feature in enumerate(features_second_plot):
        if feature == 'Age':
            # For continuous variable 'Age', use histplot
            sns.histplot(data=df, x=feature, hue='TSH_Level_binned', multiple='stack', ax=axes2[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='TSH_Level_binned', ax=axes2[i])

        axes2[i].set_title(f'Distribution of {feature} by TSH_Level')
        axes2[i].set_xlabel(feature)
        axes2[i].set_ylabel('Count')

    if len(features_second_plot) % 2 != 0:
        fig2.delaxes(axes2[-1])

    # Adjust layout for the second plot
    plt.tight_layout()
    plt.show()


def plot_t3_relationships_with_bins(df):
    """
    Plots histograms with T3_Level binned, comparing it against other features.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Define bin edges for T3_Level (can be adjusted as per requirement)
    t3_bins = [0, 1.25, 2, 2.75, 3.5]
    t3_labels = ['0-1.25', '1.25-2', '2-2.75', '2.75-3.5']
    df['T3_Binned'] = pd.cut(df['T3_Level'], bins=t3_bins, labels=t3_labels)

    # Define the features for the first plot (Age, Gender, Country, Ethnicity, Diabetes, TSH_Level)
    features_first_plot = ['Age', 'Gender', 'Country', 'Ethnicity', 'Diabetes']

    # Define the features for the second plot (Family_History, Radiation_Exposure, Iodine_Deficiency, Smoking, Obesity)
    features_second_plot = ['Family_History', 'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking', 'Obesity']

    # Create the first figure with subplots
    fig1, axes1 = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
    axes1 = axes1.flatten()

    # Plot the first set of features (continuous and categorical variables)
    for i, feature in enumerate(features_first_plot):
        if feature == 'Age' or feature == 'TSH_Level':
            # For continuous variables like Age and TSH_Level, use histplot
            sns.histplot(data=df, x=feature, hue='T3_Binned', multiple='stack', ax=axes1[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='T3_Binned', ax=axes1[i])

        axes1[i].set_title(f'Distribution of {feature} by T3_Binned')
        axes1[i].set_xlabel(feature)
        axes1[i].set_ylabel('Count')

    if len(features_first_plot) % 2 != 0:
        fig1.delaxes(axes1[-1])

    # Adjust layout for the first plot
    plt.tight_layout()
    plt.show()

    # Create the second figure with subplots
    fig2, axes2 = plt.subplots(nrows=3, ncols=2, figsize=(18, 15))
    axes2 = axes2.flatten()

    # Plot the second set of features (categorical variables)
    for i, feature in enumerate(features_second_plot):
        sns.countplot(data=df, x=feature, hue='T3_Binned', ax=axes2[i])
        axes2[i].set_title(f'Distribution of {feature} by T3_Binned')
        axes2[i].set_xlabel(feature)
        axes2[i].set_ylabel('Count')

    if len(features_second_plot) % 2 != 0:
        fig2.delaxes(axes2[-1])

    # Adjust layout for the second plot
    plt.tight_layout()
    plt.show()


def plot_t4_relationships_with_bins(df):
    """
    Plots histograms with T4_Level binned, comparing it against other features.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Define bin edges for T4_Level (can be adjusted as per requirement)
    t4_bins = [4.5, 6.37, 8.24, 10.12, 12]
    t4_labels = ['4.5-6.37', '6.37-8.24', '8.24-10.12', '10.12-12']
    df['T4_Binned'] = pd.cut(df['T4_Level'], bins=t4_bins, labels=t4_labels)

    # Define the features for the first plot (Age, Gender, Country, Ethnicity, Diabetes, TSH_Level)
    features_first_plot = ['Age', 'Gender', 'Country', 'Ethnicity', 'Diabetes', 'TSH_Level']

    # Define the features for the second plot (Family_History, Radiation_Exposure, Iodine_Deficiency, Smoking, Obesity)
    features_second_plot = ['Family_History', 'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking', 'Obesity']

    # Create the first figure with subplots
    fig1, axes1 = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
    axes1 = axes1.flatten()

    # Plot the first set of features (continuous and categorical variables)
    for i, feature in enumerate(features_first_plot):
        if feature == 'Age' or feature == 'TSH_Level':
            # For continuous variables like Age and TSH_Level, use histplot
            sns.histplot(data=df, x=feature, hue='T4_Binned', multiple='stack', ax=axes1[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='T4_Binned', ax=axes1[i])

        axes1[i].set_title(f'Distribution of {feature} by T4_Binned')
        axes1[i].set_xlabel(feature)
        axes1[i].set_ylabel('Count')

    # Adjust layout for the first plot
    plt.tight_layout()
    plt.show()

    # Create the second figure with subplots
    fig2, axes2 = plt.subplots(nrows=3, ncols=2, figsize=(18, 15))
    axes2 = axes2.flatten()

    # Plot the second set of features (categorical variables)
    for i, feature in enumerate(features_second_plot):
        sns.countplot(data=df, x=feature, hue='T4_Binned', ax=axes2[i])
        axes2[i].set_title(f'Distribution of {feature} by T4_Binned')
        axes2[i].set_xlabel(feature)
        axes2[i].set_ylabel('Count')

    if len(features_second_plot) % 2 != 0:
        fig2.delaxes(axes2[-1])

    # Adjust layout for the second plot
    plt.tight_layout()
    plt.show()


def plot_nodule_size_relationships_with_bins(df):
    """
    Plots histograms with Nodule_Size binned, comparing it against other features.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Define bin edges for Nodule_Size (can be adjusted as per requirement)
    nodule_bins = [0, 1.25, 2.5, 3.75, 5]
    nodule_labels = ['0-1.25', '1.25-2.5', '2.5-3.75', '3.75-5']
    df['Nodule_Binned'] = pd.cut(df['Nodule_Size'], bins=nodule_bins, labels=nodule_labels)

    # Define the features for the first plot (Age, Gender, Country, Ethnicity)
    features_first_plot = ['Age', 'Gender', 'Country', 'Ethnicity']

    # Define the features for the second plot (TSH_Level, T3_Level, T4_Level)
    features_second_plot = ['TSH_Level', 'T3_Level', 'T4_Level']

    # Define the features for the third plot (Family_History, Radiation_Exposure, Iodine_Deficiency, Smoking, Obesity, Diabetes)
    features_third_plot = ['Family_History', 'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking', 'Obesity',
                           'Diabetes']

    # Create the first figure with subplots
    fig1, axes1 = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    axes1 = axes1.flatten()

    # Plot the first set of features (Age, Gender, Country, Ethnicity)
    for i, feature in enumerate(features_first_plot):
        if feature == 'Age':
            # For continuous variables, use histplot
            sns.histplot(data=df, x=feature, hue='Nodule_Binned', multiple='stack', ax=axes1[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='Nodule_Binned', ax=axes1[i])

        axes1[i].set_title(f'Distribution of {feature} by Nodule_Binned')
        axes1[i].set_xlabel(feature)
        axes1[i].set_ylabel('Count')

    # Adjust layout for the first plot
    plt.tight_layout()
    plt.show()

    # Create the second figure with subplots
    fig2, axes2 = plt.subplots(nrows=1, ncols=3, figsize=(18, 5))
    axes2 = axes2.flatten()

    # Plot the second set of features (TSH_Level, T3_Level, T4_Level)
    for i, feature in enumerate(features_second_plot):
        sns.histplot(data=df, x=feature, hue='Nodule_Binned', multiple='stack', ax=axes2[i], bins=20)
        axes2[i].set_title(f'Distribution of {feature} by Nodule_Binned')
        axes2[i].set_xlabel(feature)
        axes2[i].set_ylabel('Count')

    # Adjust layout for the second plot
    plt.tight_layout()
    plt.show()

    # Create the third figure with subplots
    fig3, axes3 = plt.subplots(nrows=3, ncols=2, figsize=(18, 15))
    axes3 = axes3.flatten()

    # Plot the third set of features (Family_History, Radiation_Exposure, Iodine_Deficiency, Smoking, Obesity, Diabetes)
    for i, feature in enumerate(features_third_plot):
        sns.countplot(data=df, x=feature, hue='Nodule_Binned', ax=axes3[i])
        axes3[i].set_title(f'Distribution of {feature} by Nodule_Binned')
        axes3[i].set_xlabel(feature)
        axes3[i].set_ylabel('Count')

    # Adjust layout for the third plot
    plt.tight_layout()
    plt.show()


def plot_thyroid_cancer_risk_distribution(df):
    """
    Plots the distribution of the 'Thyroid_Cancer_Risk' column and compares it with other features in the dataframe.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Create the first plot for Thyroid_Cancer_Risk distribution
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='Thyroid_Cancer_Risk', ax=ax1)
    ax1.set_title('Distribution of Thyroid Cancer Risk')
    ax1.set_xlabel('Thyroid Cancer Risk')
    ax1.set_ylabel('Count')

    # Create the second plot with Thyroid_Cancer_Risk vs. Age, Gender, Country, Ethnicity
    fig2, axes2 = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    axes2 = axes2.flatten()
    features_second_plot = ['Age', 'Gender', 'Country', 'Ethnicity']

    for i, feature in enumerate(features_second_plot):
        if feature == 'Age':
            # For continuous variables, use histplot
            sns.histplot(data=df, x=feature, hue='Thyroid_Cancer_Risk', multiple='stack', ax=axes2[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='Thyroid_Cancer_Risk', ax=axes2[i])

        axes2[i].set_title(f'{feature} by Thyroid Cancer Risk')
        axes2[i].set_xlabel(feature)
        axes2[i].set_ylabel('Count')

    # Adjust layout for the second plot
    plt.tight_layout()
    plt.show()

    # Create the third plot with Thyroid_Cancer_Risk vs. TSH_Level, T3_Level, T4_Level, Nodule_Size
    fig3, axes3 = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    axes3 = axes3.flatten()
    features_third_plot = ['TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size']

    for i, feature in enumerate(features_third_plot):
        sns.histplot(data=df, x=feature, hue='Thyroid_Cancer_Risk', multiple='stack', ax=axes3[i], bins=20)
        axes3[i].set_title(f'{feature} by Thyroid Cancer Risk')
        axes3[i].set_xlabel(feature)
        axes3[i].set_ylabel('Count')

    # Adjust layout for the third plot
    plt.tight_layout()
    plt.show()

    # Create the fourth plot with Thyroid_Cancer_Risk vs. Family_History, Radiation_Exposure, Iodine_Deficiency, Smoking, Obesity, Diabetes
    fig4, axes4 = plt.subplots(nrows=3, ncols=2, figsize=(18, 15))
    axes4 = axes4.flatten()
    features_fourth_plot = ['Family_History', 'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking', 'Obesity',
                            'Diabetes']

    for i, feature in enumerate(features_fourth_plot):
        sns.countplot(data=df, x=feature, hue='Thyroid_Cancer_Risk', ax=axes4[i])
        axes4[i].set_title(f'{feature} by Thyroid Cancer Risk')
        axes4[i].set_xlabel(feature)
        axes4[i].set_ylabel('Count')

    # Adjust layout for the fourth plot
    plt.tight_layout()
    plt.show()


def plot_diagnosis_distribution(df):
    """
    Plots the distribution of the 'Diagnosis' column and compares it with other features in the dataframe.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Create the first plot for Diagnosis distribution
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x='Diagnosis', ax=ax1)
    ax1.set_title('Distribution of Diagnosis')
    ax1.set_xlabel('Diagnosis')
    ax1.set_ylabel('Count')

    # Create the second plot with Diagnosis vs. Age, Gender, Country, Ethnicity, Thyroid_Cancer_Risk
    fig2, axes2 = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))
    axes2 = axes2.flatten()
    features_second_plot = ['Age', 'Gender', 'Country', 'Ethnicity', 'Thyroid_Cancer_Risk']

    for i, feature in enumerate(features_second_plot):
        if feature == 'Age':
            # For continuous variables, use histplot
            sns.histplot(data=df, x=feature, hue='Diagnosis', multiple='stack', ax=axes2[i], bins=20)
        else:
            # For categorical variables, use countplot
            sns.countplot(data=df, x=feature, hue='Diagnosis', ax=axes2[i])

        axes2[i].set_title(f'{feature} by Diagnosis')
        axes2[i].set_xlabel(feature)
        axes2[i].set_ylabel('Count')

    # Adjust layout for the second plot
    plt.tight_layout()
    plt.show()

    # Create the third plot with Diagnosis vs. TSH_Level, T3_Level, T4_Level, Nodule_Size
    fig3, axes3 = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    axes3 = axes3.flatten()
    features_third_plot = ['TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size']

    for i, feature in enumerate(features_third_plot):
        sns.histplot(data=df, x=feature, hue='Diagnosis', multiple='stack', ax=axes3[i], bins=20)
        axes3[i].set_title(f'{feature} by Diagnosis')
        axes3[i].set_xlabel(feature)
        axes3[i].set_ylabel('Count')

    # Adjust layout for the third plot
    plt.tight_layout()
    plt.show()

    # Create the fourth plot with Diagnosis vs. Family_History, Radiation_Exposure, Iodine_Deficiency, Smoking, Obesity, Diabetes
    fig4, axes4 = plt.subplots(nrows=3, ncols=2, figsize=(18, 15))
    axes4 = axes4.flatten()
    features_fourth_plot = ['Family_History', 'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking', 'Obesity',
                            'Diabetes']

    for i, feature in enumerate(features_fourth_plot):
        sns.countplot(data=df, x=feature, hue='Diagnosis', ax=axes4[i])
        axes4[i].set_title(f'{feature} by Diagnosis')
        axes4[i].set_xlabel(feature)
        axes4[i].set_ylabel('Count')

    # Adjust layout for the fourth plot
    plt.tight_layout()
    plt.show()


def plot_box_whisker(df):
    """
    Creates a box-whisker plot for each column: Diagnosis, Age, Gender, Country, Ethnicity,
    Thyroid_Cancer_Risk, TSH_Level, T3_Level, T4_Level, Nodule_Size, Family_History,
    Radiation_Exposure, Iodine_Deficiency, Smoking, Obesity, Diabetes.

    Parameters:
    df (pandas.DataFrame): DataFrame containing the relevant columns.

    Returns:
    None
    """
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Create the first plot with numerical columns: TSH_Level, T3_Level, T4_Level, Nodule_Size, Age
    fig1, axes1 = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))
    axes1 = axes1.flatten()
    numerical_features = ['TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size', 'Age']

    for i, feature in enumerate(numerical_features):
        sns.boxplot(data=df, x='Diagnosis', y=feature, ax=axes1[i])
        axes1[i].set_title(f'{feature} by Diagnosis')
        axes1[i].set_xlabel('Diagnosis')
        axes1[i].set_ylabel(feature)

    # Adjust layout for the first plot
    plt.tight_layout()
    plt.show()

    # Create the second plot with categorical columns: Gender, Country, Ethnicity, Thyroid_Cancer_Risk
    fig2, axes2 = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    axes2 = axes2.flatten()
    categorical_features = ['Gender', 'Country', 'Ethnicity', 'Thyroid_Cancer_Risk']

    for i, feature in enumerate(categorical_features):
        sns.boxplot(data=df, x='Diagnosis', y=feature, ax=axes2[i])
        axes2[i].set_title(f'{feature} by Diagnosis')
        axes2[i].set_xlabel('Diagnosis')
        axes2[i].set_ylabel(feature)

    # Adjust layout for the second plot
    plt.tight_layout()
    plt.show()

    # Create the third plot with binary categorical columns: Family_History, Radiation_Exposure,
    # Iodine_Deficiency, Smoking, Obesity, Diabetes
    fig3, axes3 = plt.subplots(nrows=3, ncols=2, figsize=(18, 15))
    axes3 = axes3.flatten()
    binary_features = ['Family_History', 'Radiation_Exposure', 'Iodine_Deficiency',
                       'Smoking', 'Obesity', 'Diabetes']

    for i, feature in enumerate(binary_features):
        sns.boxplot(data=df, x='Diagnosis', y=feature, ax=axes3[i])
        axes3[i].set_title(f'{feature} by Diagnosis')
        axes3[i].set_xlabel('Diagnosis')
        axes3[i].set_ylabel(feature)

    # Adjust layout for the third plot
    plt.tight_layout()
    plt.show()


def create_plots(df, unprocessed_df):
    #plot_age_histogram(df)
    #plot_age_gender_distribution(df)
    #plot_country_distribution(unprocessed_df)
    #plot_age_distribution_by_country(unprocessed_df)
    #plot_population_pyramids(unprocessed_df)
    #plot_age_distribution_by_ethnicity(unprocessed_df)
    #plot_ethnicity_gender_histogram(unprocessed_df)
    #plot_ethnicity_distribution_by_country(unprocessed_df)
    #plot_family_history_relationships(unprocessed_df)
    #plot_radiation_exposure_relationships(unprocessed_df)
    #plot_iodine_deficiency_relationships(unprocessed_df)
    #plot_smoking_relationships(unprocessed_df)
    #plot_obesity_relationships(unprocessed_df)
    #plot_diabetes_relationships(unprocessed_df)
    #plot_tsh_binned_relationships(unprocessed_df)
    #plot_t3_relationships_with_bins(unprocessed_df)
    #plot_t4_relationships_with_bins(unprocessed_df)
    #plot_nodule_size_relationships_with_bins(unprocessed_df)
    #plot_thyroid_cancer_risk_distribution(unprocessed_df)
    #plot_diagnosis_distribution(unprocessed_df)
    print()


def plot_boxplots(df):
    """
    Plots box-and-whisker plots for specified columns in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to plot.

    Columns to plot:
    - 'Age'
    - 'TSH_Level'
    - 'T3_Level'
    - 'T4_Level'
    - 'Nodule_Size'
    """
    columns = ['Age', 'TSH_Level', 'T3_Level', 'T4_Level', 'Nodule_Size']

    # Ensure the DataFrame contains the specified columns
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame.")

    # Create a figure and axes
    fig, axes = plt.subplots(nrows=1, ncols=len(columns), figsize=(20, 5))

    # Generate boxplots for each column
    for ax, col in zip(axes, columns):
        ax.boxplot(df[col].dropna(), patch_artist=True)
        ax.set_title(f'{col} Distribution')
        ax.set_ylabel(col)
        ax.grid(True)

    # Adjust layout
    plt.tight_layout()
    plt.show()


def outlier_analysis(unprocessed_df):
    plot_boxplots(unprocessed_df)


def plot_model_comparison(scores_dict):
    # Extract model names and corresponding scores
    models = list(scores_dict.keys())
    validation_scores = [scores_dict[model][0] for model in models]
    accuracy_scores = [scores_dict[model][1] for model in models]

    # Define the position of the bars on the x-axis
    x = np.arange(len(models))
    width = 0.35  # Width of the bars

    # Create the plot
    fig, ax = plt.subplots()
    bars1 = ax.bar(x - width / 2, validation_scores, width, label='Validation Score')
    bars2 = ax.bar(x + width / 2, accuracy_scores, width, label='Accuracy Score')

    # Add labels, title, and custom x-axis tick labels
    ax.set_xlabel('Models')
    ax.set_ylabel('Scores')
    ax.set_title('Model Comparison: Validation and Accuracy Scores')
    ax.set_xticks(x)
    ax.set_xticklabels(models)
    ax.legend()

    # Attach a text label above each bar displaying its height
    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    add_labels(bars1)
    add_labels(bars2)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
