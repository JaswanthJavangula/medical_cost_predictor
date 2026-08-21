from setuptools import logging, setup, find_packages
from typing import List
from src.exception.exception import MedicalCostException
from src.logging import logger

def get_requirements(file_path:str)->List[str]:
    requirements_final : List[str] = []
    try:
        with open("requirements.txt", "r") as file :
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_final.append(requirement)
    except Exception as e:
        raise MedicalCostException(f"Error reading requirements file: {e}")
    logger.info(f"Requirements read successfully from {file_path}: {requirements_final}")
    return requirements_final

setup(
    name= "medical_cost",
    version= "0.0.1",
    author= "Jaswanth Javangula",
    author_email= "javanguj@csp.edu",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
    )