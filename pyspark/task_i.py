import mysql.connector
from pyspark.sql import SparkSession


def ingestion_parquet():

    spark = SparkSession.builder.config("spark.jars", "/Users/coder/Downloads/mysql-connector-java-8.0.22.jar")\
        .master("local[*]").appName("CoinIngestion").getOrCreate()
    df = spark.read.parquet("./data/temp.parquet")
    df.show()
    df.write.format('jdbc').options(
        url='jdbc:mysql://localhost:3306/db_coin_test?useSSL=false&useLegacyDatetimeCode=false&serverTimezone=UTC',
        driver='com.mysql.cj.jdbc.Driver',
        dbtable='bitcoin',
        user='root',
        password='password').save(mode="append")


def connection_localhost_example():
    cnx = mysql.connector.connect(user='***', password='***',
                                  host='localhost',
                                  database='db_coin_test')
    query = "INSERT INTO bitcoin (spread,high,low,volume) VALUES (28834.54,29365.52,28822.22,21650.31268086);"
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cnx.close()


url = "jdbc:mysql://localhost/db_coin_test"
username = "***"
password = "***"
driver = "com.mysql.jdbc.Driver"
db_table = 'coin'


import requests
import http.client
from os import path
import csv


def get_bitcoin_requests():
	url = "https://bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com/indices/global/ticker/BTCUSD"
	headers = {
		"X-RapidAPI-Key": "***",
		"X-RapidAPI-Host": "***"
	}
	response = requests.get(url, headers=headers)
	data = response.json()
	save_json(data)
	return data


def get_bitcoin_http():
	conn = http.client.HTTPSConnection("bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com")
	headers = {
		'X-RapidAPI-Key': "***",
		'X-RapidAPI-Host': "***"
	}

	conn.request("GET", "/indices/global/ticker/BTCUSD", headers=headers)

	res = conn.getresponse()
	data = res.read()
	return data.decode("utf-8")


def save_json(json_data):
	is_file = path.isfile('./data/data_stream.csv')
	with open('./data/data_stream.csv', 'a', newline='') as csv_file:
		headers = json_data.keys()
		writer = csv.DictWriter(csv_file, fieldnames=headers)
		if not is_file:
			writer.writeheader()
		writer.writerow(json_data)
