#!/bin/bash

if [[ -d ./functions/java8 ]]
then
  echo Cleaning target dir
  rm -r functions/src/hello_world/target
  echo Cleaning functions dir
  rm -r ./functions/java8
  mkdir functions/java8
  echo Building project
  docker run -it --rm --name maven-build -v $(pwd)/functions/src/hello_world/:/usr/src/hello_world -w /usr/src/hello_world maven:3.3-jdk-8 mvn install
  echo moving jar
  mv functions/src/hello_world/target/helloworld-1.0.jar functions/java8
else
  echo Current directory, $(pwd), is not project root
fi
