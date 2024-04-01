import requests

PASSED = "Passed"
NOT_PASSED = "Not passed"

MESSAGE = ''  # Message that will be compared in HTTP responses
verifications = []  # A list that used in verify_response() to collect results of verification (Trues and Falses)


def send_request(payload):
    # There will be your request from Burp

    # Set 'payload' in the request. For example, set 'payload' in the HTTP request in the JSON body:
    # burp0_json={"confirmCode": payload}

    # Set the response to the request to the 'response' variable and then send it to verify_response()
    response = ""
    verify_response(response)


def verify_response(response):
    http = False
    message = False

    # Verification HTTP response status codes
    # E.g. if you want the server to respond with HTTP 403 Forbidden for requests with malicious characters.
    # You can remove this check if it is not required in your autotests
    if str(response.status_code) == "200":
        http = False
    elif str(response.status_code) == "403":
        http = True
    else:
        http = False

    # Verification for the expected MESSAGE in the HTTP response body
    # E.g. if it is vulnerable it will respond "Success", if not the response will not contain that message.
    # You can remove this check if it is not required in your autotests
    if MESSAGE in str(response.text):
        message = False
    else:
        message = True

    # Appending the results of checks to the verifications[] so that you can later check it for PASSED or NOT PASSED checks.
    # You can change the items that will be added to the list,
    # for example, adding "HTTP_CODE":response.status_code and output the HTTP code of each check
    verifications.append(
        {
            "HTTP": http,
            "MESSAGE": message
        }
    )


# Checking for PASSED or NOT PASSED checks and printing results
def print_results():
    for verification in verifications:
        if verification["HTTP"] is False or verification["MESSAGE"] is False:
            print(NOT_PASSED, verification)
        else:
            print(PASSED, verification)


with open("resources/payloads.txt", 'r') as payloads:
    for payload in payloads.readlines():
        send_request(payload.replace('\n', ''))

print_results()
