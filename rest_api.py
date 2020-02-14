# @frappe.whitelist()
# def send_sms_sim(self=None, parameters=None, short_url=None, smsdata=None, data=None):
#     print("in queue")
#     try:
#         import http.client
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
#         req_data = {}
#         url = ''
#         for p in parameters:
#             url = p.get('sms_gateway_url')
#             post = p.get('post')
#             req_data = {
#                 "send_from": p.get('send_from')
#             }
#             break
#
#         conn = http.client.HTTPSConnection("myapt.pk")
#         # req_data["send_from"] = "00923154503880"
#         req_data['send_to'] = d['MessageTo']
#         req_data['send_text'] = d['MessageText']
#
#         # payload = {"send_to": data['send_to'], "send_text": data['send_text'], "send_from": data['send_from']}
#         payload = json.dumps(req_data)
#         headers = {'content-type': "application/json"}
#
#         conn.request("POST", url, payload, headers)
#
#         res = conn.getresponse()
#         # d = res.read()
#
#         if res.status == 200:
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
#             logs.sms_api = 'Sim'
#             logs.short_url = short_url
#             logs.date_time = frappe.utils.now()
#             logs.save(ignore_permissions=True)
#             return res.status
#
#     except Exception as ex:
#       # sendsmsresponse(self=self, url=url, smsdata=smsdata, data=data)
#         print(ex)
#
# @frappe.whitelist()
# def send_sms_long_code(self=None, parameters=None, short_url=None, smsdata=None, data=None):
#     print("in queue")
#     try:
#         # session = requests.Session()
#         request_data = {}
#         url = ''
#         for p in parameters:
#             url = p.get('sms_gateway_url')
#             post = p.get('post')
#             request_data = {
#                 "originator": p.get('originator'),
#                 "username": p.get('username'),
#                 "password": p.get('password'),
#                 "action": p.get('action')
#             }
#             break
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
#
#         request_data['messagedata'] = d['MessageText']
#         request_data['recipient'] = d['MessageTo']
#         req = json.dumps(request_data)
#
#         response = requests.post(url, data=req, headers={'content-type': "application/json"})
#
#         print(response.status_code)
#         if response.status_code == 200:
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
#             logs.sms_api = 'Long Code'
#             logs.short_url = short_url
#             logs.date_time = frappe.utils.now()
#             logs.save(ignore_permissions=True)
#             return response
#
#     except Exception as ex:
#         print(ex)