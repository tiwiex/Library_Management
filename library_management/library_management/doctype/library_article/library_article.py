# Copyright (c) 2023, Taiwo Akinosho and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class LibraryArticle(WebsiteGenerator):
	def before_save(self):
		self.route = f'{self.article_name}'
