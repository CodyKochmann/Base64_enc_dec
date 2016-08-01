# Sublime Text plugin created to encode/decode the current text to/from base64
# Name: Base64_encode_decode.py
# Author: Cody L. Kochmann
# Date: Tue Apr 28 07:51:09 PDT 2015
# Version: 1.0

import sublime, sublime_plugin, base64

class encode_base64Command(sublime_plugin.TextCommand):
	def run(self, edit):
		allcontent = sublime.Region(0, self.view.size())
		all_text = (self.view.substr(allcontent))
		b64_text = str(base64.b64encode(bytes(all_text, 'utf-8')))[2:-1]
		self.view.replace(edit, allcontent, b64_text)

class decode_base64Command(sublime_plugin.TextCommand):
	def run(self, edit):
		allcontent = sublime.Region(0, self.view.size())
		all_text = (self.view.substr(allcontent))
		#converted_text = str(base64.b64decode(all_text))[2:-1].replace("","")
		converted_text = base64.b64decode(all_text).decode('unicode_escape')
		self.view.replace(edit, allcontent, converted_text)
