from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    this function will read the requirements file and return a list of requirements
    '''
    requirements=['pandas', 'numpy', 'scikit-learn','seaborn']
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Sharayu',
    author_email='sharayu.sathe123@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)


