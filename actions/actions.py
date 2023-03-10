import requests
from typing import Any, Text, Dict, List
from datetime import date
import datetime
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List, Union
from xmlrpc.client import ServerProxy
import xmlrpc.client
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class CountEntriesAction(Action):
    def name(self) -> Text:
        return "act_quatation_num"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'

        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        table_name = 'crm.lead'
        # Select data from the table 'sale.order'
        record_count = models.execute_kw(db, uid, password, table_name, 'search_count', [[]])

        # Logout of the XMLRPC session
        # server.common.logout(session_id)

        # Print the record count
        message = (f"There are {record_count} Quotations.")
        
        dispatcher.utter_message(text=message)

        return []


class TypeEntriesAction(Action):
    def name(self) -> Text:
        return "act_quatation_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'

        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        table_name = 'crm.lead'
        # Select data from the table 'sale.order'
        qn = SlotSet('quotation_number',tracker.latest_message['text'])
        print(qn)
        print(qn['value'])
        qnt = tracker.get_slot('quotation_number')
        print(qnt)
        record_count = models.execute(db, uid, password, table_name, 'search_read', [('quotation_no', '=', qnt)])
        print(record_count[0]['quotation_type'])
        # Logout of the XMLRPC session
        # server.common.logout(session_id)

        # Print the record count
        message = (f"This Quotation type is {record_count[0]['quotation_type']}")
        
        dispatcher.utter_message(text=message)

        return []

class RevEntriesAction(Action):
    def name(self) -> Text:
        return "act_quatation_rev"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'

        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        table_name = 'crm.lead'
        # Select data from the table 'sale.order'
        qn = SlotSet('quotation_number',tracker.latest_message['text'])
        print(qn)
        print(qn['value'])
        qnt = tracker.get_slot('quotation_number')
        print(qnt)
        record_count = models.execute(db, uid, password, table_name, 'search_read', [('quotation_no', '=', qnt)])
        print(record_count[0]['expected_revenue'])
        # Logout of the XMLRPC session
        # server.common.logout(session_id)

        # Print the record count
        message = (f"This Quotation revenue is {record_count[0]['expected_revenue']}")
        
        dispatcher.utter_message(text=message)

        return []


class RevCountEntriesAction(Action):
    def name(self) -> Text:
        return "act_quatation_rev_count"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'

        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        table_name = 'crm.lead'
        # Select data from the table 'sale.order'
        qn = SlotSet('quotation_number',tracker.latest_message['text'])
        print(qn)
        print(qn['value'])
        qnt = tracker.get_slot('quotation_number')
        print(qnt)
        record_count = models.execute(db, uid, password, table_name, 'search_read', [('quotation_no', '=', qnt)])
        print(record_count[0]['id'])
        countid = record_count[0]['id']
        # Logout of the XMLRPC session
        # server.common.logout(session_id)
        record_count = models.execute(db, uid, password, table_name, 'search_count', [('standard_crm_id', '=', countid)])
        # Print the record count
        message = (f"This Quotation revision count is {record_count}")
        
        dispatcher.utter_message(text=message)

        return []


class RevCountEntriesAction(Action):
    def name(self) -> Text:
        return "act_quatation_count_today"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'

        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        table_name = 'crm.lead'
        # Select data from the table 'sale.order'
        # qn = SlotSet('quotation_number',tracker.latest_message['text'])
        # print(qn)
        # print(qn['value'])
        # qnt = tracker.get_slot('quotation_number')
        # print(qnt)
        today = str(date.today())
        print(today)
        record_count = models.execute(db, uid, password, table_name, 'search_count', [('create_date', '>=', today)])
        print(record_count)
        # date = datetime_obj.date()
        # print(date)
        # Logout of the XMLRPC session
        # server.common.logout(session_id)
        # Print the record count
        message = (f"The Quotation today are {record_count}")
        
        dispatcher.utter_message(text=message)

        return []

class RevCountEntriesAction(Action):
    def name(self) -> Text:
        return "act_quatation_count_month"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'

        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        table_name = 'crm.lead'
        # Select data from the table 'sale.order'
        # qn = SlotSet('quotation_number',tracker.latest_message['text'])
        # print(qn)
        # print(qn['value'])
        # qnt = tracker.get_slot('quotation_number')
        # print(qnt)
        today = date.today()
        start_of_month = today.replace(day=1)
        end_of_month = start_of_month.replace(day=28)
        record_count = models.execute_kw(
            db, uid, password, 'crm.lead', 'search_count',
            [[('create_date', '>=', start_of_month.strftime('%Y-%m-%d %H:%M:%S')),
              ('create_date', '<=', end_of_month.strftime('%Y-%m-%d %H:%M:%S'))]]
        )
        # date = datetime_obj.date()
        # print(date)
        # Logout of the XMLRPC session
        # server.common.logout(session_id)
        # Print the record count
        message = (f"The Quotation in this month are {record_count}")
        
        dispatcher.utter_message(text=message)

        return []


class RevCountEntriesAction(Action):
    def name(self) -> Text:
        return "act_quatation_count_quaterly"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'

        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        table_name = 'crm.lead'
        # Select data from the table 'sale.order'
        # qn = SlotSet('quotation_number',tracker.latest_message['text'])
        # print(qn)
        # print(qn['value'])
        # qnt = tracker.get_slot('quotation_number')
        # print(qnt)
        today = datetime.date.today()
        quarter_start_month = (today.month - 1) // 3 * 3 + 1
        start_of_quarter = datetime.date(today.year, quarter_start_month, 1)

        # format the datetime object as a string
        start_of_quarter_str = start_of_quarter.strftime('%Y-%m-%d %H:%M:%S')
        end_of_quarter = start_of_quarter.replace(month=start_of_quarter.month+2, day=28).strftime('%Y-%m-%d %H:%M:%S')

        # Search for records created within the current quarter
        record_count = models.execute_kw(db, uid, password, table_name, 'search_count',
                                        [[('create_date', '>=', start_of_quarter_str), ('create_date', '<=', end_of_quarter)]])
        # date = datetime_obj.date()
        # print(date)
        # Logout of the XMLRPC session
        # server.common.logout(session_id)
        # Print the record count
        message = (f"The Quotation quaterly are {record_count}")
        
        dispatcher.utter_message(text=message)

        return []

class ActionQuotationStatus(Action):
    def name(self) -> Text:
        return "action_quotation_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        order_id = tracker.get_slot("quotation_number")
        import xmlrpc.client
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'
        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        # order_id = 'Q00004'

        # Select data from the table 'sale.order'
        sale_orders = models.execute_kw(db, uid, password, 'crm.lead', 'search_read',
                                        [],
                                        {'fields': ["quotation_no","stage_id"]})


        for sale_order in sale_orders:
            if sale_order["quotation_no"] == order_id:
                j = sale_order["stage_id"]
            # print("Sale order status: ", sale_order['status'])
        message = (f"The status of Quotation {order_id} is {j[1]} ")
        dispatcher.utter_message(text=message)
        # print(j[1])
        return []

class ActionQuotationStatus(Action):
    def name(self) -> Text:
        return "action_quotation_name_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        order_id = tracker.get_slot("quotation_number")
        order_id = order_id.upper()
        import xmlrpc.client
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'
        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        # order_id = 'Q00004'
        domain = []
        if order_id:
            domain = [[['quotation_no','=',order_id]]]
        # Select data from the table 'sale.order'
        sale_orders = models.execute_kw(db, uid, password, 'crm.lead', 'search_read',
                                    [[]],
                                    {'fields': ["quotation_no","partner_id","street"]})
        for sale_order in sale_orders:
            if sale_order["quotation_no"] == order_id:
                j = sale_order["partner_id"]
                k = sale_order["street"]
            # print("Sale order status: ", sale_order['status'])
        message = (f"The Quotation {order_id} Customer name is {j[1]} and address is {k} ")
        dispatcher.utter_message(text=message)
        # print(j[1])
        return []

class ActionQuotationStatus(Action):
    def name(self) -> Text:
        return "action_latest_quotation_revision"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the quotation number and convert it to uppercase
        search_quotation = tracker.get_slot("quotation_number").upper()
        
        import xmlrpc.client
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'
        
        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        
        # Search for the latest revision of the given quotation number
        quotation_ids = models.execute_kw(db, uid, password, 'crm.lead', 'search',
                                          [[('quotation_no', 'ilike', search_quotation)]])
        latest_revision = None
        
        for quotation_id in quotation_ids:
            quotation = models.execute_kw(db, uid, password, 'crm.lead', 'read',
                                           [quotation_id],
                                           {'fields': ['quotation_no']})[0]['quotation_no']
            parts = quotation.split(" - ")
            # print(parts)
            if len(parts) == 2:
                quotation_num, revision_num = parts
                if latest_revision is None or revision_num > latest_revision:
                    latest_revision = revision_num
                    # print("hey i am ",latest_revision)
                    break
            else:
                latest_revision = None
        # print("hey ",latest_revision)
        
        # Construct the message to be sent back to the user
        if latest_revision is not None:
            latest_quotation = f"{search_quotation} - {latest_revision}"
            message = f"The latest quotation for {search_quotation} is: {latest_quotation}"
        else:
            message = f"No quotation found for {search_quotation}"
        
        dispatcher.utter_message(text=message)

        return []

class ActionQuotationStatus(Action):
    def name(self) -> Text:
        return "list_latest_quotations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the quotation number and convert it to uppercase
        
        import xmlrpc.client
        url = 'http://192.168.0.145:3333/'
        db = 'mar6_rapid_bevtech'
        username = 'admin'
        password = 'admin'
        
        # Authenticate and create the XML-RPC client
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        table_name = 'crm.lead'
        # Search for the latest revision of the given quotation number
        record_count = models.execute_kw(db, uid, password, table_name, 'search_read',[], {'fields': ['quotation_no','expected_revenue'],'order': 'create_date desc', 'limit': 10})
        print(record_count)
        quotation_number = record_count[0]['quotation_no']
        # date = datetime_obj.date()
        # print(date)
        # Logout of the XMLRPC session
        # server.common.logout(session_id)
        # Print the record count
        message1 = (f"The latest 10 quotations are:")
        message3 = []
        message3.append(message1)
        for i in range(0,10):
            message2 = (f"{i+1} : Quotation Number is {record_count[i]['quotation_no']} and it's revenue is {record_count[i]['expected_revenue']}")
            message3.append(message2)
            print(message3)
        message4 = (f"{message3}")
        result = message4.replace("[","")
        result1 = result.replace("]","")
        result2 = result1.replace('"',"")
        result3 = result2.replace(',',"\n")
        result4 = result3.replace("'","")
        dispatcher.utter_message(text=result4)
        return []