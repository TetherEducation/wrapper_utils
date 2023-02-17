import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tether_utils",
    install_requires=["boto3", "drf-jwt", "djangorestframework", "drf-yasg"],
    version="1.1.1",
    author="Claudio Sanchez",
    author_email="claudiosanchez@consiliumbots.com",
    description=("Thin wrapper for Tether Utils / AWS SNS and Others"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TetherEducation/wrapper-utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
)

# 0.0.1 -> Initial
# 1.0.1 -> Initial
# 1.1.0 -> fix for str message
# 1.1.1 -> fix on json import


