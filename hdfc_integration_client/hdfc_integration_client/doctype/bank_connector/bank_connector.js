// Copyright (c) 2023, Aerele Technologies Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on("Bank Connector", {
	onload(frm) {
		frm.set_query("bank_account", function (doc) {
			return {
				filters: {
					company: doc.company,
					is_company_account: 1
				},
			};
		});
	}
});
