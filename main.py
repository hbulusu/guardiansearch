#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2

import webapp2
import util
import google.appengine.api.urlfetch as urlfetch

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class TestHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('Hello world!')

class HomeHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('<form method="get" action="/search"><input name="tag"/><input type="hidden" name="page" value=1><input type="submit"/></form>')

class SearchHandler(webapp2.RequestHandler):
  def get(self):
    tag = self.request.get('tag')
    page = self.request.get('page')
    next_page = int(page) + 1
    prev_page = int(page) - 1
    template_values = {'keyword': tag}
    num_results, search_results, pages = util.search(tag, page)
    template_values['search_results'] = search_results
    template_values['page'] = int(page)
    template_values['next_page'] = next_page
    template_values['prev_page'] = prev_page
    template_values['num_results'] = num_results
    template_values['pages'] = pages
    template = jinja_environment.get_template('main.html')
    self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', HomeHandler), ('/search', SearchHandler)], debug=True)
