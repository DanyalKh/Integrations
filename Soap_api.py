from zeep import Client, Transport
# from requests import Session
from zeep.cache import SqliteCache
# from requests.auth import HTTPBasicAuth

def soap_api():

    wsdl = "http://cbs.zong.com.pk/ReachCWSv2/CorporateSMS.svc?wsdl"
    # session = Session()
    # session.auth = HTTPBasicAuth('923120825064', 'Zong@123')
    client = Client(wsdl, transport=Transport(cache=SqliteCache()))
    # , session = session

    request_data = {
        'loginId' : '923120825064',
        'loginPassword' : 'Zong@123',
        'Destination': '923322184147',
        'Message': 'Hello Paelu',
        'Mask': 'MyApt',
        'UniCode': 0,
        'ShortCodePrefered': 'n'
        }

    response = client.service.QuickSMS(request_data)
    if response.find('Submitted Successfully'):
        pass
    print response

if __name__ == '__main__':
    try:

        soap_api()

    except Exception as e:
        print e

# @frappe.whitelist()
# def send_sms_masking(self=None, parameters=None, short_url=None, smsdata=None, data=None):
#     from zeep import Client, Transport
#     from zeep.cache import SqliteCache
#
#     print("in queue")
#     try:
#
#         request_data = {}
#         url = ''
#         for p in parameters:
#             url = p.get('sms_gateway_url')
#             post = p.get('post')
#             request_data = {
#                 "loginId": p.get('loginId'),
#                 "loginPassword": p.get('loginPassword'),
#                 "Mask": p.get('Mask'),
#                 "UniCode": p.get('UniCode'),
#                 "ShortCodePrefered": p.get('ShortCodePrefered')
#             }
#             break
#
#         # url = 'http://cbs.zong.com.pk/ReachCWSv2/CorporateSMS.svc?wsdl'
#         client = Client(url, transport=Transport(cache=SqliteCache()))
#         # request_data = {
#         #     'loginId': '923120825064',
#         #     'loginPassword': 'Zong@123',
#         #     'Mask': 'MyApt',
#         #     'UniCode': 0,
#         #     'ShortCodePrefered': 'n'
#         # }
#
#         if isinstance(data, unicode):
#             self = json.loads(self)
#         else:
#             self = self
#
#         if isinstance(data, unicode):
#             d = json.loads(data)
#         else:
#             d = data
#
#         request_data['Destination'] = d['MessageTo']
#         request_data['Message'] = d['MessageText']
#         response = client.service.QuickSMS(request_data)
#         print(response)
#         if response.find("Successfully"):
#             logs = frappe.new_doc("SMS Logs")
#             logs.sms_status = 'Sent'
#             try:
#                 logs.reference_type = self.doctype
#                 logs.reference_name = self.name
#             except Exception as ex:
#                 logs.reference_type = self.get('doctype')
#                 logs.reference_name = self.get('name')
#             logs.message_to = d['MessageTo']
#             logs.message_text = d['MessageText']
#             logs.sms_api = 'Masking'
#             logs.short_url = short_url
#             logs.date_time = frappe.utils.now()
#             logs.save(ignore_permissions=True)
#             return response
#
#     except Exception as e:
#         pass
