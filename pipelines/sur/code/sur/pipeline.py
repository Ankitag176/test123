from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sur.config.ConfigStore import *
from sur.udfs.UDFs import *
from prophecy.utils import *
from sur.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Source_0 = Source_0(spark)
    df_Filter_1 = Filter_1(spark, df_Source_0)
    df_OrderBy_1 = OrderBy_1(spark, df_Filter_1)
    df_Reformat_1 = Reformat_1(spark, df_OrderBy_1)
    df_Filter_2 = Filter_2(spark, df_Reformat_1)
    df_SetOperation_1 = SetOperation_1(spark, df_Filter_2)

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
