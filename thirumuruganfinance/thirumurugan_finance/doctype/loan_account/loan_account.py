# -*- coding: utf-8 -*-
# Copyright (c) 2022, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import add_months, getdate

class LoanAccount(Document):
	def on_submit(self):
		for i in range(1, (self.period + 1)):

			new_doc = frappe.new_doc("Payment Schedule")
			new_doc.loan_account = self.name
			new_doc.division = self.division
			new_doc.due_number = i
			new_doc.due_date = getdate(add_months(self.posting_date, (i-1))).replace(day=self.due_date)
			new_doc.due_amount = self.due_amount
			new_doc.save()
			new_doc.submit()
			last_date = new_doc.due_date

	def on_cancel(self):
		if frappe.db.exists("Payment Schedule", {"loan_account": self.name, "is_paid": 1}):
			frappe.throw("You cannot cancel a loan account for which dues are already paid")
