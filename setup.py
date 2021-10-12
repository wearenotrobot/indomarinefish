"""
https://packaging.python.org/tutorials/packaging-projects/
https://www.markdownguide.org/cheat-sheet/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indonesian-fishproduction",
    version="0.1.1",
    author="mizan toyyibun",
    author_email="untirta.mizan62@gmail.com",
    description="This package will give us information about the marine fish production"
                "in Indonesia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wearenotrobot/indomarinefish",
    project_urls={
        "Bug Tracker": "https://github.com/wearenotrobot/indomarinefish",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
