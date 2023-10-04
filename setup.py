from setuptools import setup, find_packages
from typing import List


PROJECT_NAME = 'Food Delivery Time Prediction'
VERSION = '0.0.1'
DESCRIPTION = 'This machine learning project predict the food delivery time based on various parameter like location, road traffic, type of vehicle etc.'
AUTHOR_NAME = 'Mohammad Azkar'
AUTHOR_EMAIL = 'azkar7307@gmail.com'

REQUIREMENTS_FILE_NAME = 'requirements.txt'
HYPHEN_E_DOT = '-e .'


# Requirements.txt file open
#read


def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace('\n', '') for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        
        return requirement_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires=get_requirements_list()
     )




