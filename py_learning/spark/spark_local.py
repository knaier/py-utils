from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import functions as f
from pyspark.sql.types import StringType
import datetime
import faulthandler



faulthandler.enable()

sc = SparkContext("local", "Example")

spark = SparkSession.builder.getOrCreate()

@f.udf("string")
def month_as_int(month):
    print(month)
    if True:
        return "NA"
    try:
        month_number = datetime.datetime.strptime(month, "%b").month
        return month_number
    except Exception:
        return -1

data = spark.read.format("csv").option("sep", ";").option("inferSchema", "true").option("header", "true").load(
    "../../resources/bank/bank.csv")
data = data.withColumn("month_as_int", month_as_int("month"))
data.show()

data.printSchema()

# register a udf
# spark.udf.register("monthAsInt", month_as_int)

# temp view
# data.createOrReplaceTempView("bank_data_view")

# dataWithMonth = spark.sql('''
# select *, monthAsInt(month) as month_as_int from bank_data_view
# ''')
# dataWithMonth.show()
# dataWithMonth.printSchema()

# distutils issue on 3.12
# pd = data.toPandas()
# print(pd)
