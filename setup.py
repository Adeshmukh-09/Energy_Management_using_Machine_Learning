from setuptools import find_packages, setup
from typing import List

Hyphen_E_Dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

    if Hyphen_E_Dot in requirements:
        requirements.remove(Hyphen_E_Dot)

    return requirements

setup(
    name = "Energy_Management_using_Machine_Learning",
    version = "0.0.1",
    author = "arjundeshmukh",
    author_email = "arjundeshmukh757575@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)