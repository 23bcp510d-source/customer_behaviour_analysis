
import csv
import os
import unittest


class TestCustomerBehaviourProject(unittest.TestCase):

    def test_required_files_exist(self):
        required_files = [
            "customer_shopping_behavior.csv",
            "customer_behaviour_query.sql",
            "README.md",
        ]

        for file_path in required_files:
            with self.subTest(file=file_path):
                self.assertTrue(
                    os.path.isfile(file_path),
                    f"Required file is missing: {file_path}",
                )

    def test_csv_has_header_and_data(self):
        path = "customer_shopping_behavior.csv"

        with open(path, newline="", encoding="utf-8-sig") as file:
            sample = file.read(8192)
            file.seek(0)

            try:
                dialect = csv.Sniffer().sniff(
                    sample, delimiters=",\t;|"
                )
            except csv.Error:
                dialect = csv.excel_tab

            reader = csv.reader(file, dialect)
            header = next(reader, None)

            self.assertIsNotNone(header, "CSV header is missing")
            self.assertGreater(
                len(header), 1, "CSV should have multiple columns"
            )

            rows = sum(1 for row in reader if row)
            self.assertGreater(rows, 0, "CSV contains no data rows")


if __name__ == "__main__":
    unittest.main()
