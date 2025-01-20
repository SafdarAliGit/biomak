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
        {"label": "I-JAN", "fieldname": "january_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-FEB", "fieldname": "february_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-MAR", "fieldname": "march_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-APR", "fieldname": "april_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-MAY", "fieldname": "may_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-JUN", "fieldname": "june_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-JUL", "fieldname": "july_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-AUG", "fieldname": "august_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-SEP", "fieldname": "september_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-OCT", "fieldname": "october_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-NOV", "fieldname": "november_investment", "fieldtype": "Data", "width": 120},
        {"label": "I-DEC", "fieldname": "december_investment", "fieldtype": "Data", "width": 120},
        {"label":"Tot. Inv", "fieldname": "total_investment", "fieldtype": "Data", "width": 120},
        {"label":"Tot. Target", "fieldname": "total_sale_target", "fieldtype": "Data", "width": 120},

        # Monthly Sales Fields
        {"label": "S-JAN", "fieldname": "january_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-FEB", "fieldname": "february_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-MAR", "fieldname": "march_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-APR", "fieldname": "april_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-MAY", "fieldname": "may_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-JUN", "fieldname": "june_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-JUL", "fieldname": "july_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-AUG", "fieldname": "august_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-SEP", "fieldname": "september_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-OCT", "fieldname": "october_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-NOV", "fieldname": "november_sales", "fieldtype": "Data", "width": 120},
        {"label": "S-DEC", "fieldname": "december_sales", "fieldtype": "Data", "width": 120},
        {"label":"Tot. Sales", "fieldname": "total_sale", "fieldtype": "Data", "width": 120},
        {"label":"Remaining Sale", "fieldname": "remaining_sale", "fieldtype": "Data", "width": 120},
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
    i.medical_store AS medical_store,
    -- Sum for each month from Investment Entry Items
    SUM(CASE WHEN i.month = 'January' THEN i.investment_amount ELSE 0 END) AS january_investment,
    SUM(CASE WHEN i.month = 'February' THEN i.investment_amount ELSE 0 END) AS february_investment,
    SUM(CASE WHEN i.month = 'March' THEN i.investment_amount ELSE 0 END) AS march_investment,
    SUM(CASE WHEN i.month = 'April' THEN i.investment_amount ELSE 0 END) AS april_investment,
    SUM(CASE WHEN i.month = 'May' THEN i.investment_amount ELSE 0 END) AS may_investment,
    SUM(CASE WHEN i.month = 'June' THEN i.investment_amount ELSE 0 END) AS june_investment,
    SUM(CASE WHEN i.month = 'July' THEN i.investment_amount ELSE 0 END) AS july_investment,
    SUM(CASE WHEN i.month = 'August' THEN i.investment_amount ELSE 0 END) AS august_investment,
    SUM(CASE WHEN i.month = 'September' THEN i.investment_amount ELSE 0 END) AS september_investment,
    SUM(CASE WHEN i.month = 'October' THEN i.investment_amount ELSE 0 END) AS october_investment,
    SUM(CASE WHEN i.month = 'November' THEN i.investment_amount ELSE 0 END) AS november_investment,
    SUM(CASE WHEN i.month = 'December' THEN i.investment_amount ELSE 0 END) AS december_investment,
    COALESCE(SUM(i.investment_amount),0) AS total_investment,
    COALESCE(SUM(i.sale_target),0) AS total_sale_target,
    
    -- Sum for each month from Sales Entry Items
    SUM(CASE WHEN i.month = 'January' THEN i.sale_amount ELSE 0 END) AS january_sales,
    SUM(CASE WHEN i.month = 'February' THEN i.sale_amount ELSE 0 END) AS february_sales,
    SUM(CASE WHEN i.month = 'March' THEN i.sale_amount ELSE 0 END) AS march_sales,
    SUM(CASE WHEN i.month = 'April' THEN i.sale_amount ELSE 0 END) AS april_sales,
    SUM(CASE WHEN i.month = 'May' THEN i.sale_amount ELSE 0 END) AS may_sales,
    SUM(CASE WHEN i.month = 'June' THEN i.sale_amount ELSE 0 END) AS june_sales,
    SUM(CASE WHEN i.month = 'July' THEN i.sale_amount ELSE 0 END) AS july_sales,
    SUM(CASE WHEN i.month = 'August' THEN i.sale_amount ELSE 0 END) AS august_sales,
    SUM(CASE WHEN i.month = 'September' THEN i.sale_amount ELSE 0 END) AS september_sales,
    SUM(CASE WHEN i.month = 'October' THEN i.sale_amount ELSE 0 END) AS october_sales,
    SUM(CASE WHEN i.month = 'November' THEN i.sale_amount ELSE 0 END) AS november_sales,
    SUM(CASE WHEN i.month = 'December' THEN i.sale_amount ELSE 0 END) AS december_sales,
    COALESCE(SUM(i.sale_amount), 0) AS total_sale,
    (COALESCE(SUM(i.investment_amount),0) - COALESCE(SUM(i.sale_amount), 0)) AS remaining_sale
    
    FROM
        `tabInvestment Entry Items` i
    GROUP BY
        i.doctor, i.town, i.mso, i.rm, i.medical_store;
    """
    query_result = frappe.db.sql(query, as_dict=True)
    data.extend(query_result)
    return data
