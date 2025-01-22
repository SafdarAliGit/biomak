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
        {"label": "Tot. Inv", "fieldname": "total_investment", "fieldtype": "Data", "width": 120},
        {"label": "Tot. Target", "fieldname": "total_sale_target", "fieldtype": "Data", "width": 120},

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
        {"label": "Tot. Sales", "fieldname": "total_sale", "fieldtype": "Data", "width": 120},
        {"label": "Remaining Sale", "fieldname": "remaining_sale", "fieldtype": "Data", "width": 120},
        {"label": "Remaining Amount", "fieldname": "remaining_amount", "fieldtype": "Data", "width": 120},
        {"label": "Multiplier", "fieldname": "multiplier", "fieldtype": "Data", "width": 120},

    ]

    return columns


def get_conditions(filters):
    """
    Constructs the WHERE clause conditions based on the filters provided.

    Args:
        filters (dict): A dictionary of filter keys and values.

    Returns:
        str: A string representing the WHERE clause conditions.
        dict: A dictionary of parameters for the query.
    """
    conditions = []
    parameters = {}

    if filters.get("doctor"):
        conditions.append("i.doctor = %(doctor)s")
        parameters["doctor"] = filters["doctor"]

    if filters.get("mso"):
        conditions.append("i.mso = %(mso)s")
        parameters["mso"] = filters["mso"]

    if filters.get("rm"):
        conditions.append("i.rm = %(rm)s")
        parameters["rm"] = filters["rm"]
    if filters.get("year"):
        conditions.append("i.year = %(year)s")
        parameters["year"] = filters["year"]
    # if filters.get("plan"):
    #     conditions.append("i.plan = %(plan)s")
    #     parameters["plan"] = filters["plan"]

    where_clause = " AND ".join(conditions) if conditions else "1=1"
    return where_clause, parameters


def get_data(filters):
    """
    Fetches investment and sales data based on provided filters.

    Args:
        filters (dict): A dictionary of filter keys and values.

    Returns:
        list: A list of dictionaries containing aggregated data.
    """
    where_clause, parameters = get_conditions(filters)

    query = f"""
        SELECT
            i.doctor AS doctor,
            i.town AS town,
            i.mso AS mso,
            i.rm AS rm,
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

            (COALESCE(SUM(i.sale_target),0) - COALESCE(SUM(i.sale_amount), 0)) AS remaining_sale,
            ROUND((COALESCE(SUM(i.sale_target),0) - COALESCE(SUM(i.sale_amount), 0))/AVG(CASE WHEN i.sale_multiplier <> 0 THEN i.sale_multiplier ELSE NULL END),2) AS remaining_amount,
            AVG(CASE WHEN i.sale_multiplier <> 0 THEN i.sale_multiplier ELSE NULL END) AS multiplier

        FROM
            `tabInvestment Entry Items` i
        WHERE
            {where_clause}
        GROUP BY
            i.doctor, 
            i.town, 
            i.mso, 
            i.rm
        HAVING
            -- Ensure at least one column is non-zero
            total_investment != 0 OR
            total_sale_target != 0 OR
            total_sale != 0 OR
            january_investment != 0 OR
            february_investment != 0 OR
            march_investment != 0 OR
            april_investment != 0 OR
            may_investment != 0 OR
            june_investment != 0 OR
            july_investment != 0 OR
            august_investment != 0 OR
            september_investment != 0 OR
            october_investment != 0 OR
            november_investment != 0 OR
            december_investment != 0 OR
            january_sales != 0 OR
            february_sales != 0 OR
            march_sales != 0 OR
            april_sales != 0 OR
            may_sales != 0 OR
            june_sales != 0 OR
            july_sales != 0 OR
            august_sales != 0 OR
            september_sales != 0 OR
            october_sales != 0 OR
            november_sales != 0 OR
            december_sales != 0 
            
            
        """

    query_result = frappe.db.sql(query, parameters, as_dict=True)

    return query_result
