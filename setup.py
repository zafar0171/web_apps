from setuptools import setup, find_packages

setup(
    name="demo-jformat",
    version="0.0.1",
    description='Reformats files to stdout",' ,
    install_requires= ["click","coloroma"],
    entry_points="""
    [console_scripts]
    jformat=jformat.main:main
    """,
    author="Modassir",
    author_email="",
    packages=find_packages()

)