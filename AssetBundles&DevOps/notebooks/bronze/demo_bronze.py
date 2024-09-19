# Databricks notebook source
from framework.common_functions.metadata_functions import (
    read_yaml,
    get_spark_type_mapping,
)

if __name__ == "__main__":
    print("This is bronze")
    print(read_yaml("bronze_columns"))
    print(get_spark_type_mapping())
