import zipfile
import logging
import glob
import os

logging.getLogger().setLevel(logging.INFO)
file_directory = os.path.dirname(os.path.abspath(__file__))


def zip_data_product(folder: str):
    with zipfile.ZipFile(
        os.path.join(file_directory, f"data_product{folder}.zip"), "w"
    ) as f:
        data_product_directory = os.path.join(file_directory, folder)
        for file in (
            glob.glob(os.path.join(
                data_product_directory, "application", "*.py"))
            + glob.glob(os.path.join(data_product_directory, "requirements.txt"))
            + glob.glob(os.path.join(data_product_directory, "metadata", "*"))
        ):
            logging.info(file)
            f.write(file)


def main():
    zip_data_product("_example_2")


if __name__ == "__main__":
    main()
