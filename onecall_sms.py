import requests

url = "http://www.onecall.no/minesider/sendsmsnow-test.php"
session_id = ""
onecall_id = ""

post_data = { 
    "avsender":"96900000",
    "nummer":"96900000",
    "numsms":"1",
    "smsmsg":"test fra python"
}
headers = {'content-type': 'application/x-www-form-urlencoded'}
cookies = {'PHPSESSID': session_id, 'onecall': onecall_id}
post_response = requests.post(
    url=url, data=post_data, headers=headers, cookies=cookies)
print post_response
print post_response.text
