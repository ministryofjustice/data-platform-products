import zipfile
import glob


def zip_data_product(folder: str):
    with zipfile.ZipFile(f"data_product_{folder}.zip", "w") as f:
        for file in glob.glob(f"./{folder}/application/*") + glob.glob(f"./{folder}/requirements.txt"):
            f.write(file)


def main():
    zip_data_product("_example_2")


if __name__ == "__main__":
    main()
