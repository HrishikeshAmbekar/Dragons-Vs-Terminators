import os
import shutil


def custom_make_archive(source, destination):
    shutil.make_archive(destination, 'zip', source)


if __name__ == "__main__":
    source = os.path.dirname(os.path.abspath(__file__))
    source = os.path.dirname(source)
    destination_dir = os.path.dirname(source)
    destination = os.path.join(destination_dir, "{}".format("dragon_solutions"))

    custom_make_archive(source, destination)
