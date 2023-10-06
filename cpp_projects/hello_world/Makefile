CXX := clang++
CXXFLAGS := -std=c++17 -Wall
TARGET := ./a.out
SOURCES := hello_world.cpp

build: $(TARGET)

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCES)

run:
	$(TARGET)
