from aws_cdk import core
from aws_cdk import aws_lambda as lambda_
import csv
from os import path


class DeployStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        functions = self.get_functions()
        for function in functions:
            runtime_string = function.get('runtime')
            location = function.get('location')
            runtime = getattr(lambda_.Runtime, runtime_string)
            handler = function.get('handler')
            code = self.get_code_from_asset(location)
            lambda_.Function(self, f"serverless-metrics-{runtime_string}", runtime=runtime, handler=handler,
                             code=code, tracing=lambda_.Tracing.ACTIVE)

    @staticmethod
    def get_code_from_asset(location):
        asset_path = path.join('../functions', location)
        return lambda_.Code.from_asset(asset_path)

    @staticmethod
    def get_inline_code(location):
        with open(path.join('../functions/', location)) as fn_file:
            code = fn_file.read()
            return lambda_.Code.from_inline(code)

    @staticmethod
    def get_functions():
        with open('../functions/functions.csv') as csvfile:
            reader = csv.DictReader(csvfile, skipinitialspace=True)
            return [{k: v for k, v in row.items()} for row in reader]

