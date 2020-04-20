import setuptools

setuptools.setup(
    name="create_python_app",
    version="1.0.0",
    description="utility for creating python projects",
    packages=setuptools.find_packages('src'),
    package_dir={'':'src'})