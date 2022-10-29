# -*- coding: utf-8 -*-
# Copyright (c) 2022, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LoanReceipt(Document):
	def on_submit(self):
		doc = frappe.get_doc("Payment Schedule", {"loan_account": self.loan_account, "due_number": self.due_number})
		if not doc:
			frappe.throw("The entered due number is invalid")
		doc.is_paid = 1
		doc.loan_receipt = self.name
		doc.save()
