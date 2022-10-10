import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='solidity-antpool',
    version='0.0.1',
    description='ANTPOOLs application programming interface (API) allows users to access and control their accounts using custom written software.',
    url='https://github.com/jonova-coder/antpool-solidity',
    author='Jordi Pascual Dalmau',
    author_email='pascual.dalmau@gmail.com',
    packages=['AntPool'],
    install_requires=['requests'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
