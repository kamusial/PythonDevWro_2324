import csv
from dataclasses import make_dataclass

import fastavro
from pydantic_avro.base import AvroBase


def read_csv(filepath: str) -> list[dict]:
    with open(filepath) as file:
        return list(csv.DictReader(file))


def create_schema_based_on_data(data: list[dict]):
    columns = list(data[0].keys())
    cols_with_types = [(col, str) for col in columns]
    schema_class = make_dataclass("SchemaClass", cols_with_types, bases=(AvroBase,))
    avro_schema = schema_class.avro_schema()
    return avro_schema


def csv_to_avro(data_filepath: str, output_filepath: str):
    data = read_csv(data_filepath)
    schema = create_schema_based_on_data(data)
    with open(output_filepath, "wb") as file:
        fastavro.writer(file, schema, data)


if __name__ == '__main__':
    csv_to_avro("data/data.csv", "data/output.avro")
