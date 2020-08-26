import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="telget", # Replace with your own username
    version="1.0.0",
    author="MrPythonBlog",
    author_email="mrpython@gmail.com",
    description="a Small Library for Getting Info About Telegram Usernames .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrpythonblog/telget",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
