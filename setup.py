import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="despell-feldmanngreg",
    version="0.1.0",
    author="Greg Feldmann",
    author_email="gfeldman@tpg.com.au",
    description="Introduces spelling/typing errors into text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phosgene89/despell",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
