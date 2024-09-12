from pathlib import Path
from setuptools import find_packages, setup

# Read the long description from the README file
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8")

setup(
    name="phone_gen",
    packages=find_packages(exclude=("tests", "dev_tools")),
    url="https://github.com/tolstislon/phone-gen",
    license="MIT License",
    author="tolstislon",
    author_email="tolstislon@gmail.com",
    description="International phone number generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    use_scm_version={"write_to": "phone_gen/__version__.py"},
    setup_requires=["setuptools_scm"],
    install_requires=["string-gen>=0.1.0"],
    entry_points={
        "console_scripts": ["phone-gen=phone_gen.cli:main"],
    },
    python_requires=">=3.8",
    include_package_data=True,
    keywords=[
        "testing", "test-data", "phone-number", "phone",
        "test-data-generator"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
        "Topic :: Communications :: Telephony",
    ],
)
