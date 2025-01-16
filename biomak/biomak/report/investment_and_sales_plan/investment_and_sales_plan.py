# Copyright (c) 2025, TechVentures and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    columns = [
        {
            "label": "<b>PLAN</b>",
            "fieldname": "plan",
            "fieldtype": "Data",
            "width": 100

        },
        {
            "label": "<b>MSO</b>",
            "fieldname": "mso",
            "fieldtype": "Data",
            "width": 100

        },
        {
            "label": "<b>RM</b>",
            "fieldname": "rm",
            "fieldtype": "Data",
            "width": 100

        }
    ]
    return columns


def get_data(filters):
    data = []
    investment_entry = frappe.db.sql(
        "Select plan,mso,rm from `tabInvestment Entry`",
    )
    data.extend(investment_entry)
    return data
