import logging
import sys
import time

import smpplib.gsm
import smpplib.client
import smpplib.consts

# if you want to know what's happening
logging.basicConfig(level='DEBUG')

# number list
num_list = ['923322184147', '923333023982']
del_count = 0
client = smpplib.client.Client("smsctp3.eocean.us", 28555)

# Print when obtain message_id
client.set_message_sent_handler(
    lambda pdu: on_sent(pdu))
client.set_message_received_handler(
    lambda pdu: on_rec(pdu))

def on_rec(pdu):
    global del_count
    sys.stdout.write('delivered {}\n'.format(pdu.short_message))
    del_count += 1

def on_sent(pdu):
    global del_count
    sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id))
    # del_count += 1

client.connect()
client.bind_transceiver(system_id='maven99095', password='NBgvftrV')

for num in num_list:

    pdu = client.send_message(
        source_addr_ton=0,
        source_addr='99095',
        dest_addr_ton=1,
        destination_addr=num,
        short_message='hello12'.encode(),

    )

while len(num_list) != del_count:
    client.poll()
client.unbind()
client.disconnect()



# @frappe.whitelist()
# def send_sms_short_code(self=None, smsdata=None, short_url=None, data=None, parameters=None):
#     import xmltodict
#     print("in queue")
#     global del_count
#     try:
#
#         if isinstance(parameters, unicode):
#             parameters = json.loads(parameters)
#         else:
#             parameters = parameters
#
#         if isinstance(data, unicode):
#             d = json.loads(data)
#         else:
#             d = data
#
#         del_count = 0
#         username = ''
#         password = ''
#         client = ''
#         source_addr = ''
#         source_addr_ton = ''
#         dest_addr_ton = ''
#         destination_addr = ''
#         short_message = ''
#         registered_delivery = ''
#         alert_on_message_delivery = ''
#
#         request_data = {}
#         url = ''
#         for p in parameters:
#             url = p.get('sms_gateway_url')
#             post = p.get('post')
#             username = p.get('username')
#             password = p.get('password')
#             source_addr = str(p.get('originator'))
#             source_addr_ton = 0
#             dest_addr_ton = 1
#             destination_addr = str(d['MessageTo'])
#             short_message = str(d['MessageText'])
#             registered_delivery = True
#             alert_on_message_delivery = True
#
#             # request_data = {
#             #     "source_addr_ton" : 0,
#             #     "source_addr" : p.get('originator'),
#             #     "dest_addr_ton" : 1,
#             #     "destination_addr": d['MessageTo'],
#             #     "short_message": d['MessageText'],
#             #     "registered_delivery": True,
#             #     "alert_on_message_delivery": True,
#             # }
#             break
#
#         # request_data['short_message'] = d['MessageText']
#         # request_data['destination_addr'] = d['MessageTo']
#         # req = json.dumps(request_data)
#
#         def sent_handler(pdu):
#             # global del_count
#             print ("sent: ", pdu.sequence, pdu.message_id, pdu.status)
#
#         def received_handler(pdu):
#             global del_count
#             print ("delivered: ", pdu.short_message)
#             logs = ''
#             log_doc = frappe.get_all("SMS Logs", filters={'message_to': destination_addr}, order_by="creation desc", limit=1)
#
#             if len(log_doc) > 0:
#                 for l in log_doc:
#                     logs = frappe.get_doc('SMS Logs', l.name)
#
#             if len(log_doc) == 0:
#                 logs = frappe.new_doc("SMS Logs")
#
#             logs.sms_status = 'Sent'
#             id = ''
#             date = ''
#             time = ''
#             msg = pdu.short_message.split(' ')[07]
#             if msg == 'stat:DELIVRD' or msg == 'stat:ACCEPTD':
#                 id = "{0}".format(pdu.short_message.split(' ')[0].split(':')[1])
#                 date = datetime.strptime(pdu.short_message.split(' ')[6].split(':')[1], '%y%m%d%H%M').date()
#                 time = datetime.strptime(pdu.short_message.split(' ')[6].split(':')[1], '%y%m%d%H%M').time()
#             try:
#                 logs.reference_type = self.doctype
#                 logs.reference_name = self.name
#
#             except Exception as ex:
#                 logs.reference_type = self.get('doctype')
#                 logs.reference_name = self.get('name')
#
#             logs.message_to = destination_addr
#             logs.message_text = short_message
#             logs.sms_api = 'Short Code'
#             logs.confirmation_msg = ''
#             logs.sms_date = date
#             logs.sms_time = time
#             logs.id = id
#             logs.short_url = short_url
#             logs.response = pdu.short_message
#             logs.date_time = frappe.utils.now()
#             logs.save(ignore_permissions=True)
#             del_count += 1
#             # return response
#
#         try:
#             client = smpplib.client.Client(url, 28555)
#             client.set_message_sent_handler(lambda pdu: sent_handler(pdu))
#             # client.set_message_sent_handler(sent_handler)
#             client.set_message_received_handler(lambda pdu: received_handler(pdu))
#             client.connect()
#             client.bind_transceiver(system_id=username, password=password)
#
#             for num in d['num_list']:
#                 print(short_message)
#                 # for part in parts:
#                 pdu = client.send_message(
#                         source_addr_ton=source_addr_ton,
#                         source_addr=source_addr,
#                         dest_addr_ton=dest_addr_ton,
#                         destination_addr=str(num),
#                         short_message=short_message,
#                         registered_delivery=registered_delivery,
#                         alert_on_message_delivery=alert_on_message_delivery,
#                 )
#                 # pdu = client.send_message(request_data)
#                 # time.sleep(4)
#                 # client.poll()
#
#                 logs = frappe.new_doc("SMS Logs")
#                 logs.sms_status = 'Sent'
#                 try:
#                     logs.reference_type = self.doctype
#                     logs.reference_name = self.name
#                 except Exception as ex:
#                     logs.reference_type = self.get('doctype')
#                     logs.reference_name = self.get('name')
#                 logs.message_to = d['MessageTo']
#                 logs.message_text = short_message
#                 logs.sms_api = 'Short Code'
#                 logs.short_url = short_url
#                 logs.sms_status = 'Sent'
#                 logs.date_time = frappe.utils.now()
#                 logs.save(ignore_permissions=True)
#                 # time.sleep(4)
#             while len(d['num_list']) != del_count:
#                 client.poll()
#
#             client.unbind()
#             client.disconnect()
#
#         except Exception as e:
#             print(e)
#         #     finally:
#         #         # print "==client.state====", client.state
#         #         if client.state in [smpplib.consts.SMPP_CLIENT_STATE_BOUND_TX]:
#         #             # if bound to transmitter
#         #             try:
#         #                 client.unbind()
#         #             except smpplib.exceptions.UnknownCommandError as ex:
#         #                 # https://github.com/podshumok/python-smpplib/issues/2
#         #                 try:
#         #                     client.unbind()
#         #                 except smpplib.exceptions.PDUError as ex:
#         #                     pass
#         #
#         # finally:
#         #     if client:
#         #         # print "==client.state====", client.state
#         #         client.disconnect()
#                 # print "==client.state====", client.state
#
#         # response = requests.post(url, data=request_data, headers={'content-type': "application/json"})
#
#         # response = requests.post("http://smsctp3.eocean.us:24555/api?action=sendmessage&username=maven_99095&password=msol4466&recipient=923322184147&originator=99095&messagedata=Test123.")
#
#         # print(response.status_code)
#         # result = xmltodict.parse(response._content)
#         # msg = result.get('response').get('data').get('acceptreport').get('statusmessage') + ' for ' + result.get('response').get('data').get('acceptreport').get('recipient')
#         # if response.status_code == 200:
#         #     logs = frappe.new_doc("SMS Logs")
#         #     logs.sms_status = 'Sent'
#
#             # try:
#             #     logs.reference_type = self.doctype
#             #     logs.reference_name = self.name
#             # except Exception as ex:
#             #     logs.reference_type = self.get('doctype')
#             #     logs.reference_name = self.get('name')
#
#             # logs.message_to = d['MessageTo']
#             # logs.message_text = d['MessageText']
#             # logs.sms_api = 'Short Code'
#             # logs.confirmation_msg = msg
#             # logs.date_time = frappe.utils.now()
#             # logs.save(ignore_permissions=True)
#             # return response
#
#     except Exception as ex:
#         print(ex)
