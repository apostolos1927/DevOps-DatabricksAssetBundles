import yaml
from pathlib import Path
from pyspark.sql.types import (
    DoubleType,
    DateType,
    ByteType,
    ShortType,
    StructType,
    StringType,
    MapType,
    ArrayType,
    IntegerType,
    TimestampType,
    BooleanType,
    LongType,
    FloatType,
    BinaryType,
)


root_path = Path().resolve().parent.parent
metadata_path = (root_path / "src" / "framework" / "utils" / "metadata.yaml").resolve()
print("metadata_path", metadata_path)


def get_spark_type_mapping():

    return {
        "StringType": StringType(),
        "LongType": LongType(),
        "BooleanType": BooleanType(),
        "TimestampType": TimestampType(),
        "IntegerType": IntegerType(),
        "FloatType": FloatType(),
        "DoubleType": DoubleType(),
        "DateType": DateType(),
        "BinaryType": BinaryType(),
        "ByteType": ByteType(),
        "ShortType": ShortType(),
        "ArrayType": ArrayType,
        "MapType": MapType,
        "StructType": StructType,
    }


def read_yaml(entity_name: str) -> dict:
    with open(metadata_path, "r") as file:
        data = yaml.safe_load(file)[entity_name]
    return data
