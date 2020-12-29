#!/usr/bin/env python3

from aws_cdk import core

from deploy_stack import DeployStack


app = core.App()
DeployStack(app, "deploy")

app.synth()
