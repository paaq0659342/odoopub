# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Cubic ERP - Teradata SAC (<http://cubicerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Purchase Order Approve Sequence",
    "version": "1.0",
    "description": """
Adds a new sequence when the purchase order is approved.
    """,
    "author": "Cubic ERP",
    "website": "http://cubicERP.com",
    "category": "Purchase Management",
    "depends": [
    		"purchase",
            "report_geraldo",
	    ],
	"data":[
            "purchase_view.xml",
            "purchase_report.xml",
            "purchase_sequence.xml",
	    ],
    "demo_xml": [
	    ],
    "update_xml": [
	    ],
    "active": False,
    "installable": True,
    "certificate" : "",
}