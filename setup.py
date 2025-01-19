from setuptools import setup, find_packages
from pathlib import Path

# Define the current directory and load the README for the long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Setup configuration
setup(
    name='Topsis-Harsh-102203215',  
    version='1.4.9',  
    packages=find_packages(),  
    license='MIT',
    description='A Python package for TOPSIS ranking with CLI support for CSV/Excel files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Harsh Lakyan",  
    author_email='harshlakyan@gmail.com',
    install_requires=[
        'numpy>=1.21.0',  
        'pandas>=1.3.0',
    ],
    python_requires='>=3.6',  
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis_102203215:main",
        ],
    },
)
