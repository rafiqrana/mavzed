import setuptools

# def read_requirements():
#     with open('requirements.txt') as rq:
#         content = rq.read()
#         req = content.split('\n')
#     return req

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mavzed",
    version="0.0.1",
    author="Rafiq Rana",
    author_email="rafiq.rana.bd@gmail.com",
    description="A linux service that control and record ZED camera from mav commmd from transmitter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafiqrana/mavzed",
    project_urls={
        "Bug Tracker": "https://github.com/rafiqrana/mavzed/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    # include_package_data=True,
    # python_requires=">=3.6",
    # install_requires=read_requirements(),
    entry_points = {
        'console_scripts': ['mavzed=src.__main__:main'],
    },
)