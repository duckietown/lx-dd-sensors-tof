from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'tof_listener'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Duckietown',
    maintainer_email='info@duckietown.com',
    description='Duckiedrone ToF listener node (subscribes to sensor_msgs/Range topics)',
    license='None',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tof_listener_node = tof_listener.tof_listener_node:main',
        ],
    },
)
