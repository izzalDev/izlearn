from setuptools import find_packages, setup

setup(
    name='izlearn',
    packages=find_packages(exclude=['test']),
    version='0.1.0',
    description='Test buat library python',
    author='izzalDev',
    license='MIT',
    install_requires=[],    
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='test',
    long_description='halo dunia',
    long_description_content_type='text/markdown'
)