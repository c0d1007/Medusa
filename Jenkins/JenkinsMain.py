#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Jenkins import JenkinsArbitraryFileReadVulnerability
from Jenkins import JenkinsRemoteCommandExecutionVulnerability
from Jenkins import JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(JenkinsArbitraryFileReadVulnerability.medusa,Url,Values,ProxyIp)
    ThreadPool.Append(JenkinsRemoteCommandExecutionVulnerability.medusa, Url, Values, ProxyIp)
    ThreadPool.Append(JenkinsConfigurationErrorCausesUnauthorizedCodeExecutionVulnerability.medusa, Url, Values, ProxyIp)
    Prompt("Jenkins")



