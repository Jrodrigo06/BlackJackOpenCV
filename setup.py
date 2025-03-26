from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    Will return list of required imports
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n", "") for req in requirements] # Replaces the \n within the list

        if "-e ." in requirements:
            requirements.remove('-e .')

    return requirements

setup(
name='mlproject', 
version='0.0.1',
author='Jerome',
author_email = 'jeromerodrigo06@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
                 
)