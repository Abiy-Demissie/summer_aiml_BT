# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/unitree/summer_project/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/unitree/summer_project/catkin_ws/build

# Include any dependencies generated for this target.
include greenball_tracking/CMakeFiles/joystick_sub.dir/depend.make

# Include the progress variables for this target.
include greenball_tracking/CMakeFiles/joystick_sub.dir/progress.make

# Include the compile flags for this target's objects.
include greenball_tracking/CMakeFiles/joystick_sub.dir/flags.make

greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o: greenball_tracking/CMakeFiles/joystick_sub.dir/flags.make
greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o: /home/unitree/summer_project/catkin_ws/src/greenball_tracking/src/joystick_sub.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/unitree/summer_project/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o"
	cd /home/unitree/summer_project/catkin_ws/build/greenball_tracking && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o -c /home/unitree/summer_project/catkin_ws/src/greenball_tracking/src/joystick_sub.cpp

greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.i"
	cd /home/unitree/summer_project/catkin_ws/build/greenball_tracking && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/unitree/summer_project/catkin_ws/src/greenball_tracking/src/joystick_sub.cpp > CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.i

greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.s"
	cd /home/unitree/summer_project/catkin_ws/build/greenball_tracking && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/unitree/summer_project/catkin_ws/src/greenball_tracking/src/joystick_sub.cpp -o CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.s

greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o.requires:

.PHONY : greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o.requires

greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o.provides: greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o.requires
	$(MAKE) -f greenball_tracking/CMakeFiles/joystick_sub.dir/build.make greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o.provides.build
.PHONY : greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o.provides

greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o.provides.build: greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o


# Object files for target joystick_sub
joystick_sub_OBJECTS = \
"CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o"

# External object files for target joystick_sub
joystick_sub_EXTERNAL_OBJECTS =

/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: greenball_tracking/CMakeFiles/joystick_sub.dir/build.make
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /opt/ros/melodic/lib/libroscpp.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libboost_filesystem.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /opt/ros/melodic/lib/librosconsole.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /opt/ros/melodic/lib/librosconsole_log4cxx.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /opt/ros/melodic/lib/librosconsole_backend_interface.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/liblog4cxx.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libboost_regex.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /opt/ros/melodic/lib/libxmlrpcpp.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /opt/ros/melodic/lib/libroscpp_serialization.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /opt/ros/melodic/lib/librostime.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /opt/ros/melodic/lib/libcpp_common.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libboost_system.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libboost_thread.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libboost_chrono.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libboost_date_time.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libboost_atomic.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libpthread.so
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libconsole_bridge.so.0.4
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_dnn.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_gapi.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_highgui.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_ml.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_objdetect.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_photo.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_stitching.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_video.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_videoio.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_imgcodecs.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_calib3d.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_features2d.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_flann.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_imgproc.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: /usr/lib/aarch64-linux-gnu/libopencv_core.so.4.1.1
/home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub: greenball_tracking/CMakeFiles/joystick_sub.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/unitree/summer_project/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub"
	cd /home/unitree/summer_project/catkin_ws/build/greenball_tracking && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/joystick_sub.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
greenball_tracking/CMakeFiles/joystick_sub.dir/build: /home/unitree/summer_project/catkin_ws/devel/lib/greenball_tracking/joystick_sub

.PHONY : greenball_tracking/CMakeFiles/joystick_sub.dir/build

greenball_tracking/CMakeFiles/joystick_sub.dir/requires: greenball_tracking/CMakeFiles/joystick_sub.dir/src/joystick_sub.cpp.o.requires

.PHONY : greenball_tracking/CMakeFiles/joystick_sub.dir/requires

greenball_tracking/CMakeFiles/joystick_sub.dir/clean:
	cd /home/unitree/summer_project/catkin_ws/build/greenball_tracking && $(CMAKE_COMMAND) -P CMakeFiles/joystick_sub.dir/cmake_clean.cmake
.PHONY : greenball_tracking/CMakeFiles/joystick_sub.dir/clean

greenball_tracking/CMakeFiles/joystick_sub.dir/depend:
	cd /home/unitree/summer_project/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/unitree/summer_project/catkin_ws/src /home/unitree/summer_project/catkin_ws/src/greenball_tracking /home/unitree/summer_project/catkin_ws/build /home/unitree/summer_project/catkin_ws/build/greenball_tracking /home/unitree/summer_project/catkin_ws/build/greenball_tracking/CMakeFiles/joystick_sub.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : greenball_tracking/CMakeFiles/joystick_sub.dir/depend
