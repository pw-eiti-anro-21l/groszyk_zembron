import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf_file_name = 'robot1_move.urdf.xacro.xml'
    rviz2_file_name = 'robot1.rviz'
    urdf = os.path.join(
        get_package_share_directory('zad2'),
        urdf_file_name)

    rviz = os.path.join(
        get_package_share_directory('zad2'),
        rviz2_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='zad2',
            executable='no_kdl',
            name='no_kdl',
            ),
        Node(
            package='zad2',
            executable='kdl',
            name='kdl',
            )
    ])
