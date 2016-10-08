# import sys
import os
from sodapy import Socrata
import requests
import json
import oauth2

slack = SlackClient(os.environ['SLACK_OAUTH_ACCESS_TOKEN_DH'])
sclient = Socrata("sandbox.demo.socrata.com", SOCRATA_APP_TOKEN, username="fakeuser@somedomain.com", password="ndKS92mS01msjJKs")