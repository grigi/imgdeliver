'''
Setup for ImgDeliver
'''
from setuptools import find_packages, setup


def get_version(fname):
    '''Extracts __version__ from {fname}'''
    import re
    verstrline = open(fname, "rt").read()
    mob = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", verstrline, re.M)
    if mob:
        return mob.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % (fname,))


def get_requirements(fname):
    '''
    Extracts requirements from requirements-file <fname>
    '''
    reqs = open(fname, "rt").read().strip("\r").split("\n")
    requirements = [
        req for req in reqs
        if req and not req.startswith("#") and not req.startswith("--")
    ]
    return requirements


setup(
    name='imgdeliver',
    version=get_version('imgdeliver/__init__.py'),
    description='ImgDeliver - Image Deliver platform',
    long_description=open('README.rst', 'r').read(),
    author='Nickolas Grigoriadis',
    author_email='nagrigoriadis@gmail.com',
    license='MIT',
    url='https://github.com/grigi/imgdeliver',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    include_package_data=True,
    scripts=[
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
    zip_safe=False,
)
