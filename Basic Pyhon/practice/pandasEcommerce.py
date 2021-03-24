import pandas as pd
PATH = "00_data/"

#products = pd.read_csv(PATH + "olist_products_dataset.csv", encoding='utf-8-sig')
#products.head()
#products.shape
#products.info()

products = pd.read_csv(PATH + "olist_products_dataset.csv", encoding='utf-8-sig')
customers = pd.read_csv(PATH + "olist_customers_dataset.csv", encoding='utf-8-sig')
geolocation = pd.read_csv(PATH + "olist_geolocation_dataset.csv", encoding='utf-8-sig')
order_items = pd.read_csv(PATH + "olist_order_items_dataset.csv", encoding='utf-8-sig')
payments = pd.read_csv(PATH + "olist_order_payments_dataset.csv", encoding='utf-8-sig')
reviews = pd.read_csv(PATH + "olist_order_reviews_dataset.csv", encoding='utf-8-sig')
orders = pd.read_csv(PATH + "olist_orders_dataset.csv", encoding='utf-8-sig')
sellers = pd.read_csv(PATH + "olist_sellers_dataset.csv", encoding='utf-8-sig')
category_name = pd.read_csv(PATH + "product_category_name_translation.csv", encoding='utf-8-sig')

customers.head()
customers.info()
customers['customer_id'].nunique()
customers['customer_unique_id'].nunique()

customers_location = customers.groupby('customer_city').count().sort_values(by='customer_id', ascending=False)
customers_location.head(20)

customers_location = customers.groupby('customer_city')['customer_id'].nunique().sort_values(ascending=False)
customers_location.head(20)

import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)
customers_location.iplot(kind='bar', theme='white')
customers_location_top20 = customers_location.head(20)
customers_location_top20.iplot(kind='bar', theme='white')
