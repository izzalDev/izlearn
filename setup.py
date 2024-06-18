from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='izlearn',
    packages=find_packages(exclude=['test']),
    version='0.1.9',
    description='Python package for simplifying machine learning projects',
    author='izzalDev',
    license='MIT',
    install_requires=['numpy','scikit-image', 'opencv-python', 'pillow', 'matplotlib', 'tqdm'],    
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='test',
    long_description=long_description,
    long_description_content_type='text/markdown'
)