import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="earthworm-shubhamt619",
    version="0.0.5",
    author="Shubham Thakur",
    author_email="shubhamt619@gmail.com",
    description="Boilerplate for Publishing Python Packages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shubhamt619/earthworm",
    packages=setuptools.find_packages(),
    # The below are classifiers. Read more at [https://pypi.org/classifiers/]
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires='>=2.7',
)