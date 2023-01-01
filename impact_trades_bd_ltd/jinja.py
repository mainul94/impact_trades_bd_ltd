import frappe
from frappe.utils import flt


def company_wise_party_balance(company, party_type, party):
    company_wise_total_unpaid = frappe.db.sql(
        """
		select sum(debit_in_account_currency) - sum(credit_in_account_currency)
		from `tabGL Entry`
		where party_type = %s and party=%s and company = %s
		and is_cancelled = 0""",
        (party_type, party, company),
    )
    if not company_wise_total_unpaid:
        return 0
    return -1 * flt(company_wise_total_unpaid[0][0]) if party_type == "Supplier" else company_wise_total_unpaid[0][0]
