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

    # Base query
    query = """
    SELECT
        i.doctor AS doctor,
        i.town AS town,
        i.mso AS mso,
        i.rm AS rm,
        i.sale_target,
        SUM(i.amount) AS investment_amount,
        SUM(s.amount) AS sale_amount,
        s.target AS sale_target,
        s.medical_store AS medical_store
        
    FROM
        `tabInvestment Entry Items` i
    JOIN 
        `tabSales Entry Items` s ON i.mso = s.mso
    WHERE
    """

    # Initialize conditions list
    conditions = []

    # Append conditions based on filters
    if filters.get("doctor"):
        conditions.append("i.doctor = %(doctor)s")

    if filters.get("mso"):
        conditions.append("i.mso = %(mso)s")

    if filters.get("rm"):
        conditions.append("i.rm = %(rm)s")

    # Join conditions with AND and add to query
    if conditions:
        query += " AND ".join(conditions)
    else:
        # If no filters are provided, we can select all records
        query += "1=1"  # This is a placeholder for no filtering

    # Group by clause
    query += """
    GROUP BY
        i.doctor, i.town, i.mso, i.rm
    """

    # Execute the query and fetch results
    query_result = frappe.db.sql(query, filters, as_dict=True)

    # Extend data with query results
    data.extend(query_result)

    return data

