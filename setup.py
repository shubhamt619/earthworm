import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="earthworm-shubhamt619",
    version="0.0.3",
    author="Shubham Thakur",
    author_email="shubhamt619@gmail.com",
    description="Boilerplate for Publishing Python Packages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shubhamt619/earthworm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)