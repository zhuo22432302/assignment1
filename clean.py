import pandas as pd
import pickle

def clean(input_file1, input_file2):
    df_1 = pd.read_csv("respondent_contact.csv")
    df_2 = pd.read_csv("respondent_other.csv")

    df = pd.merge(df_1, df_2, how="inner", left_on="respondent_id", right_on="id")
    df = df.drop('id', axis=1)
    df = pd.DataFrame(df)
    df = df.dropna(how="any")
    df = df[df["job"].str.contains("insurance") == False]
    df = df[df["job"].str.contains("Insurance") == False]
    return df

print(clean("respondent_contact.csv","respondent_other.csv"))
print(clean("respondent_contact.csv","respondent_other.csv").shape)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='respondent_contact(CSV)')
    parser.add_argument('input', help='respondent_other(CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input)
    cleaned.to_csv(args.output, index=False)