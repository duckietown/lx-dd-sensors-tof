from setuptools import find_packages, setup

package_name = "solution"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(),
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            ["resource/" + package_name],
        ),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Duckietown",
    maintainer_email="info@duckietown.com",
    description="Duckiedrone ToF Sensors LX: student solution package",
    license="None",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
