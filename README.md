# Serverless Metrics

Purpose of this project is develop a relatively simple system that can trigger all current lambda runtimes and collect performance metrics on them.


#### Some helpful bash snippets  
This is really just for my own recollection later.

* Get all deployed functions by function name only  
`aws lambda list-functions | jq '.Functions[].FunctionName'`

* Invoking a function from cli  
`aws lambda invoke --function-name <function_name> <output_file>
`

* Building Go binary  
`d run -it -v $(pwd)/functions/go:/build -v $(pwd)/functions/src:/main  go_build:latest
`

* Building Java binaries  
`./scripts/java_8_build.sh`  
`./scripts/java_11_build.sh`
