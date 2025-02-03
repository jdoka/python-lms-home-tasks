import gzip

from scapy.layers.http import HTTPRequest, HTTPResponse
from scapy.layers.inet import TCP
from scapy.sendrecv import sniff


def get_html(payload, response):
    try:
        if b"text" in response.Content_Type:
            txt_payload = payload[payload.index(b"\r\n\r\n") + 4:]
            if response.Content_Encoding == b'gzip':
                print(txt_payload)
                if txt_payload:
                    decompressed_payload = gzip.decompress(txt_payload)
                    return decompressed_payload

        pass
    except Exception as e:
        print(e)
        pass


def process_packet(packet):
    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        print("Запрашиваемый URL:", url)
        return
    if HTTPResponse in packet:
        response: HTTPResponse = packet[HTTPResponse]
        payload = bytes(packet[TCP].payload)
        html = get_html(payload, response)
        print(html)


sniff(iface="en0", count=1000, filter="port 80", prn=process_packet, store=0)
