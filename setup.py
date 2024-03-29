from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return requirements read from the file specified by file_path.
    Each requirement should be on a separate line.
    '''

    requirements = []

    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]  # Remove newline characters
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return requirements





setup(
    name="Insurance_Predictor",
    version='0.0.1',
    author='Ashish',
    author_email='ds.ashishmishra@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)