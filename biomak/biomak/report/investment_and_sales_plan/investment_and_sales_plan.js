// Copyright (c) 2025, TechVentures and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Investment And Sales Plan"] = {
    "filters": [
        {
            "fieldname": "doctor",
            "label": __("Doctor"),
            "fieldtype": "Link",
            "options": "Doctor"
        },
        {
            "fieldname": "mso",
            "label": __("MSO"),
            "fieldtype": "Link",
            "options": "Medical Sales Officer"
        },
        {
            "fieldname": "rm",
            "label": "RM",
            "fieldtype": "Link",
            "options": "Regional Manager"
        }
    ]
};
