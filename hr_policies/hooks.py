# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "hr_policies"
app_title = "Hr Policies"
app_publisher = "Hardik gadesha"
app_description = "App for custom HR"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hardikgadesha@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hr_policies/css/hr_policies.css"
# app_include_js = "/assets/hr_policies/js/hr_policies.js"

# include js, css files in header of web template
# web_include_css = "/assets/hr_policies/css/hr_policies.css"
# web_include_js = "/assets/hr_policies/js/hr_policies.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
#doctype_js = {"Loan Application" : "public/js/loan_application.js"}
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

# Website user home page (by function)
# get_website_user_home_page = "hr_policies.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hr_policies.install.before_install"
# after_install = "hr_policies.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hr_policies.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Loan Application": {
		"validate": "hr_policies.custom_validate.validate_guarantor"
	}
}

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
			"Gate Pass-workflow_state",
			"Loan Application-workflow_state",
			"Loan Application-gross_salary",
			"Loan Application-loan_guarantor",
			"Loan Application-guarantor_details",
			"Loan Application-eligible_amount"
		]
	   ]
	]
    }
]


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hr_policies.tasks.all"
# 	],
# 	"daily": [
# 		"hr_policies.tasks.daily"
# 	],
# 	"hourly": [
# 		"hr_policies.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hr_policies.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hr_policies.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hr_policies.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hr_policies.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hr_policies.task.get_dashboard_data"
# }

