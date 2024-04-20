import setuptools

setuptools.setup(
    name='BJSCP',
    version='0.0.1',
    description='Helper for competitive programming',
    author='JUNSU BAE',
    author_email='hashilyze@gmail.com',
    url="https://github.com/hashilyze/CompetitiveProgramming",
    download_url="https://github.com/hashilyze/CompetitiveProgramming",
    pacakges=setuptools.find_packages(exclude=[]),
    keywords=["BJS", "CP", "BJSCP", "Competitive", "CompetitiveProgramming"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)