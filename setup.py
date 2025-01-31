from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            # Process all lines
            for line in lines:
                requirements = line.strip()
                # Ignore empty lines and '-e .'
                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("No requirements.txt file found")
    
    return requirements_lst  # Return the list of requirements

setup(
    name="Network_Security",
    version="0.0.1",
    author="Sujal Khant",
    author_email="sujalkhant4@gmail.com",
    packages=find_packages(), 
    install_requires=get_requirements()
)
