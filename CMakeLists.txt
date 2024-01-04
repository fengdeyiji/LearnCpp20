set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

cmake_minimum_required(VERSION 3.22) # 指定CMake的最低版本要求

project(LearnCpp20 VERSION 1.0) # 设定项目名和版本号

# 指定C++标准
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 添加子目录，此命令表示在src目录下还有CMakeLists.txt需要处理
add_subdirectory(coroutine)