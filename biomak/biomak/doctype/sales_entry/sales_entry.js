// Copyright (c) 2024, TechVentures and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Entry', {

});

frappe.ui.form.on('Sales Entry Items', {
    sales_entry_items_add: function (frm, cdt, cdn) {
        copy_values_to_child(frm, cdt, cdn);
    }
});

function copy_values_to_child(frm, cdt, cdn) {
    let row = locals[cdt][cdn]; // Access the current row

    // Extract values from the parent form
    let mso = frm.doc.mso;
    let rm = frm.doc.rm;
    let month = frm.doc.month;
    let year = frm.doc.year;

    // Validate values and throw an error if any are missing
    if (!mso || !rm || !month || !year) {
        let missingFields = [];
        if (!mso) missingFields.push("MSO");
        if (!rm) missingFields.push("RM");
        if (!month) missingFields.push("Month");
        if (!year) missingFields.push("Year");
        frappe.throw(__(`The following fields are missing: ${missingFields.join(", ")}`));
    }

    // Set values in the child table row
    frappe.model.set_value(cdt, cdn, "mso", mso);
    frappe.model.set_value(cdt, cdn, "rm", rm);
    frappe.model.set_value(cdt, cdn, "month", month);
    frappe.model.set_value(cdt, cdn, "year", year);
}
