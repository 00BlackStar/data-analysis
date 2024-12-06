import pandas as pd

def load_data():
df = pd.read_csv('data.csv')
return df
def main():
print("Data Analysis Project")
if __name__ == "__main__":
main()


def analyze_data(df):
summary = df.describe()
return summary