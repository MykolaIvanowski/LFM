from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, TimestampType, FloatType, DataType


def job_(data):
    # this is interesting solution
    # import findspark
    # findspark.add_packages('mysql:mysql-connector-java:8.0.11')

    session = SparkSession.builder.appName('quaterHourBitcoin').getOrCreate()
    schema = StructType()\
        .add('last', FloatType(), True)\
        .add('high',  FloatType(), True)\
        .add('low',  FloatType(), True)\
        .add('volume', FloatType(), True)\
        .add('volume_percent', FloatType(), True)\
        .add('timestamp', TimestampType(), True)\
        .add('display_timestamp', StringType(), True)\
        .add('display_symbol', StringType(), True)

    sc = session.sparkContext
    df = session.read.json(sc.parallelize([data]), schema=schema)

    df = df.withColumnsRenamed({"last": "spread"}) \
        .withColumnsRenamed({"timestamp": "date_timestamp"})\
        .withColumnsRenamed({"display_timestamp": "date_yyyymmdd_hhmmss"})\
        .withColumnsRenamed({"display_symbol": "symbol"})

    df.write.mode('overwrite').parquet("./data/temp.parquet")
