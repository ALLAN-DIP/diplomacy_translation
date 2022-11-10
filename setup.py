import setuptools

setuptools.setup(
    name="diplomacy_translation",
    version="0.0.1",
    author="Feng Gu",
    author_email="contact@fenggu.me",
    description="OpenAI API wrapper for DAIDE/English translation",
    long_description_content_type="text/markdown",
    url="https://github.com/ALLAN-DIP/diplomacy_translation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.7"
)
