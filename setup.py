from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip()]

setup(
    name="aeon-core",
    version="1.0.0-alpha",
    author="krisstern9-create",
    description="AEON Core — Consciousness Transfer Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krisstern9-create/aeon-core",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    test_suite="tests",
    tests_require=["pytest>=7.0.0", "pytest-cov>=4.0.0"],
)
