from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import col, sum

if __name__ == '__main__':
    spark = SparkSession.builder.master("local").appName("SparkDemoApp").config("spark.jars",
                                                                                "sqlite-jdbc-3.43.2.2.jar").getOrCreate()

    connection_url = "jdbc:sqlite:window_functions.db"
    db_properties = {"driver": "org.sqlite.JDBC"}
    employeeDF = spark.read.jdbc(connection_url, "employee_wf", properties=db_properties)
    employeeDF.show()

    window_spec_01 = Window.partitionBy(col("department_id")).orderBy(col("salary"))
    employeeDF.withColumn("total_salary", sum("salary").over(window_spec_01)).show()

    # window_spec_02 = Window.partitionBy(col("department_id")).orderBy(col("years_worked")).rowsBetween(
    #     Window.unboundedPreceding, Window.unboundedFollowing)
    # employeeDF.withColumn("prceding_following",sum("salary").over(window_spec_02)).show()
    #
    #
    # window_spec_03 = Window.partitionBy(col("department_id")).orderBy(col("years_worked")).rowsBetween(
    #     -1, Window.unboundedFollowing)
    # employeeDF.withColumn("prceding_following",sum("salary").over(window_spec_02)).show()
