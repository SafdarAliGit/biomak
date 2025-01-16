// Copyright (c) 2024, TechVentures and contributors
// For license information, please see license.txt

frappe.ui.form.on('Investment Entry', {
    // Add your parent doctype refresh or other event handlers here if needed
});

frappe.ui.form.on('Investment Entry Items', {
    investment_amount: function (frm, cdt, cdn) {
        calculate_sale_target(frm, cdt, cdn);
    },
    sale_multiplier: function (frm, cdt, cdn) {
        calculate_sale_target(frm, cdt, cdn);
    }
});

function calculate_sale_target(frm, cdt, cdn) {
    let row = locals[cdt][cdn]; // Access the current row
    let investment_amount = row.investment_amount || 0; // Default to 0 if undefined
    let sale_multiplier = row.sale_multiplier || 0; // Default to 0 if undefined
    let sale_target = investment_amount * sale_multiplier; // Calculate sale target
    frappe.model.set_value(cdt, cdn, "sale_target", sale_target); // Update the field
}
