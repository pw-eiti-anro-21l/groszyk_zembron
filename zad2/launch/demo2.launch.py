import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf_file_name = 'robot1_move.urdf.xacro.xml'
    urdf = os.path.join(
        get_package_share_directory('zad2'),
        urdf_file_name)

    rviz2_file_name = 'robot1.rviz'
    rviz2= os.path.join(
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
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher_robot',
            output='screen',
            parameters=[{
                'use_sim_time': use_sim_time,
                'robot_description': Command(['xacro', ' ', urdf])
            }]),
        # Node(
        #     package='zad2',
        #     executable='state_publisher',
        #     name='state_publisher',
        #     output='screen'),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=['-d', rviz2]),
    ])
