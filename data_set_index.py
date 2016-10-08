# import sys
import os
import requests
from sodapy import Socrata
import json

# slack = SlackClient(os.environ['SLACK_OAUTH_ACCESS_TOKEN_DH'])
category_list = [{'finance':['fifs', 'donors', 'country level', 'beneficiaries']}, {'public safety':['arrests', 'crime', 'police', 'ems', 'ucr']}, {'infrastructure':3}, {'environment':["trees", "sustainability", "renewable", "fuel", "vehicle"]}, {'demographics':5}, {'economy':6}, {'transportation':7}, {'education':8}, {'health':9}, {'housing & development':10}, {'social services':11}, {'politics':12}, {'recreation':13}]
sclient = Socrata("sandbox.demo.socrata.com", os.environ['SOCRATA_APP_TOKEN'], username="jessica.l.burns@gmail.com", password=os.environ['SOCRATA_PASS'])
domains = sclient.get('http://api.us.socrata.com/api/catalog/v1/domains')
print domains
# print 'okay'