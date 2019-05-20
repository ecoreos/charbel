# -*- coding: utf-8 -*-
# Part of abc. See LICENSE file for full copyright and licensing details.
{
    'name' : "Purchase Order From LEAD in Odoo",
    'version' : "12.0.0.0",
    'category' : "Project",
    'summary': 'This module allow to create Purchase order/ RFQ from CRM Opportunity.',
    'description' : '''
            This module allow to create Purchase order/ RFQ from CRM Opportunity, 

            also count created purchase orders.

            This module allow to create Purchase order/ RFQ from CRM Opportunity,
             also count created purchase orders.
             This module allow to create Purchase order/ RFQ from CRM Opportunity,
             also count created purchase orders.
             creat PO from lead
             PO from LEAD
             RFQ-Purchase Order From CRM Opportunity
             purchase order from LEAD
             RFQ from CRM Opportunity
             RFQ from LEAD
             RFQ from crm LEAD
             Purchase Order From CRM Opportunity
             convert lead into po
             convert lead into purchase order
             convert lead into rfq
             crm Opportunity into RFQ
             crm Opportunity into PO
             crm Opportunity into purchase order
             create RFQ from LEAD
             create RFQ from Opportunity
    ''',
    'author' : "BrowseInfo",
    'website': 'http://www.browseinfo.in',
    "price": 15,
    "currency": 'EUR',
    'depends' : ['base','crm','purchase','stock'],
    'data': [
                'security/ir.model.access.csv',
                "views/crm_opportunity_purchase_view.xml",

             ],
    'installable': True,
    'auto_install': False,
    'live_test_url': "https://youtu.be/2lVCDe0_QcM",
    "images":['static/description/Banner.png'],
    
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
