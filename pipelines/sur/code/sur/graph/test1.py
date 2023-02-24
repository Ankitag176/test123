from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from sur.config.ConfigStore import *
from sur.udfs.UDFs import *

def test1(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("text")\
        .schema(StructType([StructField("value", StringType(), True)]))\
        .text("s3://seceng-datalake-adobe-mavlink-gcp-refined-stage/", wholetext = False, lineSep = None)
