import csv
import fastavro


def csv_to_avro(data_filepath: str,
                schema_filepath: str
                ):
    with open(data_filepath) as file:
        data = list(csv.DictReader(file))
    print(data)


if __name__ == '__main__':
    csv_to_avro("data/data.csv", "")
