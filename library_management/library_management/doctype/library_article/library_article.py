# Copyright (c) 2023, Taiwo Akinosho and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LibraryArticle(Document):
	def before_save(self):
		#self.route = f'{self.article_name} {self.article_name or "taiwo"}'
		#self.routes = "taiwo"
		self.set("route", "taiwo")
