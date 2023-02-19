from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sur.config.ConfigStore import *
from sur.udfs.UDFs import *
from prophecy.utils import *
from sur.graph import *

def pipeline(spark: SparkSession) -> None:
    df_test1 = test1(spark)
    df_Filter_1 = Filter_1(spark, df_test1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/sur")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/sur")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
