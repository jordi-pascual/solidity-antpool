import setuptools

setuptools.setup(
    name="solidity-antpool",
    version="0.0.1",
    description="ANTPOOL's application programming interface (API) allows users to access and control their accounts using custom written software.",
    url="https://github.com/jonova-coder/antpool-solidity",
    author="Jordi Pascual Dalmau",
    author_email="pascual.dalmau@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    long_description="ANTPOOL's application programming interface (API) allows users to access and control their accounts using custom written software.",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
