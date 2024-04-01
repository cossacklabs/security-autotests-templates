#  Verify HTTP security headers
#
# The code performs 3 steps:
#   1. Send request
#   2. Verify responses for HTTP headers
#   3. Print results


import requests

PASSED = "Passed"
NOT_PASSED = "Not passed"

verifications = []  # A list that used in verify_response() to collect results of verification (Trues and Falses)


def send_request():
    # There will be your request from Burp

    # Set the response to the request to the 'response' variable and then send it to verify_response()
    response = ""
    verify_response(response)


def verify_response(response):
    http = False

    missing_headers = []
    headers = ['Strict-Transport-Security',
               'Content-Security-Policy',
               'X-Content-Type-Options',
               'X-Frame-Options']

    for header in headers:
        if header not in response.headers:
            missing_headers.append(header)

    missing_headers = [header for header in headers if header not in response.headers]

    if not missing_headers:
        http = True
    else:
        http = False

    # Appending the results of checks to the verifications[] so that you can later check it for PASSED or NOT PASSED checks.
    # You can change the items that will be added to the list,
    # for example, adding "HTTP_CODE":response.status_code and output the HTTP code of each check
    verifications.append(
        {
            "HTTP": http,
            "MISSING_HEADERS": missing_headers,
        }
    )


# Checking for PASSED or NOT PASSED checks and printing results
def print_results():
    for verification in verifications:
        if verification["HTTP"] is False or verification["MESSAGE"] is False:
            print(NOT_PASSED, verification)
        else:
            print(PASSED, verification)


send_request()
print_results()


