from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found") 
    
    return requirement_lst

setup(
    name = "Network security ML project",
    version="0.0.1",
    author = "Tanmay Kadbe",
    authoer_email = "tanmaykadbe32@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)