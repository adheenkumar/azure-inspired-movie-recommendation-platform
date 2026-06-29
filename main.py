from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("AzureInspiredMovieRecommendation")
    .master("local[*]")
    .getOrCreate()
)

print("=" * 50)
print("Spark Session Created Successfully")
print(f"Spark Version : {spark.version}")
print(f"Application   : {spark.sparkContext.appName}")
print("=" * 50)

spark.stop()