# Copyright (c) 2025, TechVentures and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    columns = fields = [
        {"label": "Doctor", "fieldname": "doctor", "fieldtype": "Data", "width": 150},
        {"label": "Town", "fieldname": "town", "fieldtype": "Data", "width": 120},
        {"label": "MSO", "fieldname": "mso", "fieldtype": "Data", "width": 120},
        {"label": "RM", "fieldname": "rm", "fieldtype": "Data", "width": 120},
        {"label": "Medical Store", "fieldname": "medical_store", "fieldtype": "Data", "width": 180},

        # Monthly Investment Fields
        {"label": "Investment", "fieldname": "investment_amount", "fieldtype": "Currency", "width": 120},


        # Monthly Sales Fields
        {"label": "Sales", "fieldname": "sale_amount", "fieldtype": "Currency", "width": 120},
        {"label": "Target", "fieldname": "sale_target", "fieldtype": "Currency", "width": 120},

    ]

    return columns


def get_data(filters):
    data = []
    query = """
    SELECT
    i.doctor AS doctor,
    i.town AS town,
    i.mso AS mso,
    i.rm AS rm,
    i.sale_target,
    -- Sum for each month from Investment Entry Items
    i.amount As investment_amount,
    -- Sum for each month from Sales Entry Items
    s.amount AS sale_amount
    FROM
        `tabInvestment Entry Items` i
    JOIN 
        `tabSales Entry Items` s ON i.doctor = s.doctor
    GROUP BY
        i.doctor, i.town, i.mso, i.rm
    """
    query_result = frappe.db.sql(query, as_dict=True)
    data.extend(query_result)
    return data
