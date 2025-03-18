from pyspark.sql import SparkSession
from log import log_info, log_error

def main():
    try:
        # Initialize Spark session
        spark = SparkSession.builder \
            .appName("Finance Project") \
            .getOrCreate()
        log_info("Spark session started successfully.")

        # Your Spark code here
        # ...

        # Stop the Spark session
        spark.stop()
        log_info("Spark session stopped successfully.")
    except Exception as e:
        log_error(f"Error in main: {e}")

if __name__ == "__main__":
    main()

#testing to restore staged file