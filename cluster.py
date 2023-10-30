import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_summarize_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Data summary
    data_types = df.dtypes
    shape = df.shape
    description = df.describe()
    info = df.info()
    is_null = df.isnull().sum()
    
    return df, data_types, shape, description, info, is_null

def drop_missing_values(df):
    dropdf = df.dropna()
    return dropdf

def analyze_age_distribution(df):
    plt.figure(figsize=(12, 8))
    plt.title('Age Distribution of Deaths', fontsize=15)
    sns.distplot(df.age)
    plt.tight_layout()
    plt.show()

def main():
    file_path = 'washingtonpolice.csv'
    
    df, data_types, shape, description, info, is_null = load_and_summarize_data(file_path)
    
    # Output of data summary
    print(df)
    print(data_types)
    print(shape)
    print(description)
    print(info)
    print(is_null)
    
    # Drop the missing values
    dropdf = drop_missing_values(df)
    print("-----------")
    print(dropdf.shape)

    # Additional analysis
    print(len(df) - len(dropdf))
    print(dropdf.isnull().sum())
    print(dropdf.head(4).to_string())

    print(dropdf.isna().sum())
    print("-----------")

    print(dropdf.armed.value_counts())
    
    # Analyzing the age distribution of people
    analyze_age_distribution(df)

if __name__ == "__main__":
    main()