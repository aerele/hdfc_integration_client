from . import __version__ as app_version

app_name = "hdfc_integration_client"
app_title = "Hdfc Integration Client"
app_publisher = "Aerele Technologies Private Limited"
app_description = "HDFC Integration Client"
app_email = "hello@aerele.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hdfc_integration_client/css/hdfc_integration_client.css"
# app_include_js = "/assets/hdfc_integration_client/js/hdfc_integration_client.js"

# include js, css files in header of web template
# web_include_css = "/assets/hdfc_integration_client/css/hdfc_integration_client.css"
# web_include_js = "/assets/hdfc_integration_client/js/hdfc_integration_client.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hdfc_integration_client/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}
doctype_js = {
	"Payment Request": "public/js/payment_request.js",
	"Payment Order" : "public/js/payment_order.js",
}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "hdfc_integration_client.utils.jinja_methods",
#	"filters": "hdfc_integration_client.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hdfc_integration_client.install.before_install"
after_install = "hdfc_integration_client.hdfc_integration_client.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hdfc_integration_client.uninstall.before_uninstall"
# after_uninstall = "hdfc_integration_client.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hdfc_integration_client.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

override_doctype_class = {
	"Payment Order": "hdfc_integration_client.hdfc_integration_client.override.payment_order.CustomPaymentOrder",
	"Payment Request": "hdfc_integration_client.hdfc_integration_client.override.payment_request.CustomPaymentRequest"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
	"Bank Account": {
		"validate": "hdfc_integration_client.hdfc_integration_client.doc_events.bank_account.validate_ifsc_code",
	},
	"Payment Request": {
		"validate": "hdfc_integration_client.hdfc_integration_client.doc_events.payment_request.valdidate_bank_for_wire_transfer",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"hdfc_integration_client.tasks.all"
#	],
#	"daily": [
#		"hdfc_integration_client.tasks.daily"
#	],
#	"hourly": [
#		"hdfc_integration_client.tasks.hourly"
#	],
#	"weekly": [
#		"hdfc_integration_client.tasks.weekly"
#	],
#	"monthly": [
#		"hdfc_integration_client.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "hdfc_integration_client.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	"erpnext.accounts.doctype.payment_request.payment_request.make_payment_request": "hdfc_integration_client.hdfc_integration_client.override.payment_request.make_payment_request"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "hdfc_integration_client.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hdfc_integration_client.utils.before_request"]
# after_request = ["hdfc_integration_client.utils.after_request"]

# Job Events
# ----------
# before_job = ["hdfc_integration_client.utils.before_job"]
# after_job = ["hdfc_integration_client.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"hdfc_integration_client.auth.validate"
# ]
