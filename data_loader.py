import pandas as pd

def load_data():        
    url = "https://drive.google.com/uc?export=download&id=1AzuOQPWF5PUckfjcGoHsmzs5hGJxtO7j"
    data = pd.read_csv(url)
    print(data.head(10))
    return data
if __name__ == "__main__":
    load_data()