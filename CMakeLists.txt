cmake_minimum_required(VERSION 3.4)
project(cythontest)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}  -std=c11 -g -fPIC -Wall -Wextra")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "/home/andreas/ClionProjects/cythontest/bin")

set(SOURCE_FILES fib.c fib.h)
add_executable(cythontest ${SOURCE_FILES})