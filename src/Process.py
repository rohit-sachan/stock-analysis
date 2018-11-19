import pandas as pd

price_file = "/home/rohit/PycharmProjects/stock-analysis/data/close_prediction_data/testingPrice1.pkl"


def read_test_data(pkl_file):
    return pd.read_pickle(pkl_file, compression="zip")


if __name__ == '__main__':
    data = read_test_data(price_file)
    for item in data:
        print(item)
    print(data["binNum"])
