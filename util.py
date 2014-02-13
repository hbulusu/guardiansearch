#!/usr/bin/env python
# encoding: utf-8
"""
util.py

Created by Harshini on 2013-03-17.
Copyright (c) 2013 Challa. All rights reserved.
"""

import sys
import os
import google.appengine.api.urlfetch as urlfetch
import json

def search(tag, page):
  url = 'http://content.guardianapis.com/search?page-size=50&format=json&tag=' + tag + '&page=' + page
  resp = urlfetch.fetch(url, payload=None, method='GET', headers={}, allow_truncated=False, follow_redirects=True, deadline=5, validate_certificate=False)
  search_results = []
  if resp.status_code == 200:
    obj = json.loads(resp.content)
    for result in obj['response']['results']:
      search_results.append('<a href=' + result['webUrl'] + '>' + result['webTitle'] + '</a>')
    num_results = obj['response']['total']
    pages = int(obj['response']['pages'])
  return (num_results, search_results, pages )

