#!/usr/bin/python3

import pandas as pd
import csv

def process_py():
    total_price, count = 0, 0
    with open('prices.csv', 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            try:
                price = float(data[-2])
                total_price += price
                count += 1
            except ValueError:
                continue
    return total_price / count if count > 0 else 0


def process_csv():
    total_price, count = 0, 0
    with open('prices.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                price = float(row[-2])
                total_price += price
                count += 1
            except ValueError:
                continue
    return total_price / count if count > 0 else 0



def process_pandas():
    df = pd.read_csv('prices.csv')
    return df['PRODUCT_PRICE'].mean()


def process_csv_dict():
    category_prices = {}
    category_counts = {}

    with open('prices.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['ITEM_CATEGORY_NAME']
            try:
                price = float(row['PRODUCT_PRICE'])
                if category in category_prices:
                    category_prices[category] += price
                    category_counts[category] += 1
                else:
                    category_prices[category] = price
                    category_counts[category] = 1
            except ValueError:
                continue

    avg_prices = {category: category_prices[category] / category_counts[category] for category in category_prices}
    return avg_prices


def process_pandas_groupby():
    df = pd.read_csv('prices.csv')
    return df.groupby('ITEM_CATEGORY_NAME')['PRODUCT_PRICE'].mean().to_frame()



if __name__ == "__main__":
    print("Average price using pure python: ", end='')
    print(process_py())
    print("Average price using csv module: ", end='')
    print(process_csv())
    print("Average price using pandas module: ", end='')
    print(process_pandas())
