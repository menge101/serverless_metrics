#!/bin/bash

if [[ -d ./functions/java11 ]]
then
  echo Cleaning target dir
  rm -r functions/src/hello_world/target
  echo Cleaning functions dir
  rm -r ./functions/java11
  mkdir functions/java11
  echo Building project
  docker run -it --rm --name maven-build -v $(pwd)/functions/src/hello_world/:/usr/src/hello_world -w /usr/src/hello_world maven:3.6.3-jdk-11 mvn install
  echo moving jar
  mv functions/src/hello_world/target/helloworld-1.0.jar functions/java11
else
  echo Current directory, $(pwd), is not project root
fi
