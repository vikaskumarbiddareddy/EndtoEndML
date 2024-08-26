from setuptools import find_packages,setup

from typing import List

Hypen_e_dot = '-e .'


# below code can be used when we are posting our package and for the setup file to automatically take all the requirements and install it.


"""def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements"""



setup(
    name = 'DimondPricePrediction',
    version='0.0.1',
    author='vikas kumar',
    author_email='vikaskumar.biddareddy@gmail.com',
    #install_requires = get_requirements('requirements.txt'),
    packages=find_packages() 
)