import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sysbox",
    version="0.1.1",
    author="Mark Powers",
    author_email="mpoweru@lifsys.com",
    description="Lightweight and portable sandbox runtime (code interpreter) Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vndee/sysbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "docker>=7.1.0",
        "kubernetes>=30.1.0",
    ],
)
