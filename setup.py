from setuptools import setup, find_packages

setup(
    name="dataeye",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "aisuite",
    ],
    entry_points={
        "console_scripts": [
            "dataeye-analyze=dataeye.analyzer:analyze_json"
        ]
    },
    author="Suat ATAN",
    description="A package that automatically analyzes tabular data using LLM models.",
    url="https://github.com/yourgithub/dataeye",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
