from setuptools import setup, find_packages


with open("README.md") as f:
    long_description = f.read()


setup(
    name="mini-mock-server",
    version="0.0.28",
    description="A mini mock server for http requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Igor Rodrigues",
    keywords="mock server restapi restful test development web api rest http",
    license="MIT",
    entry_points={
        "console_scripts": [
            "mini-mock-server=mini_mock_server.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(),
    python_requires=">=3.11",
)
