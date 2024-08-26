import pandas
import polars
import requests

headers = {
    "accept":
    "application/json",
    "accept-encoding":
    "gzip, deflate, br, zstd",
    "accept-language":
    "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    # "authorization":
    # "Bearer Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Imp3ay1saXZlLTEyYTkzYTc0LWE3MWItNDJlMi1hODJiLTVjZTIyNjkxYTZkZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsicHJvamVjdC1saXZlLWRkYzcxNDRlLTE2MTYtNDYzMy1iMDU4LTUxNjM5M2VlMGUxNSJdLCJleHAiOjE3MjQ1Mzg5MjIsImh0dHBzOi8vc3R5dGNoLmNvbS9zZXNzaW9uIjp7ImlkIjoic2Vzc2lvbi1saXZlLWE1NWMyNjNiLWM1NjgtNDhkNC05MzNhLWFiZjU4ZDcwYTlhMSIsInN0YXJ0ZWRfYXQiOiIyMDI0LTA4LTI0VDIxOjQ2OjExWiIsImxhc3RfYWNjZXNzZWRfYXQiOiIyMDI0LTA4LTI0VDIyOjMwOjIyWiIsImV4cGlyZXNfYXQiOiIyMDI0LTA5LTIzVDIxOjQ2OjExWiIsImF0dHJpYnV0ZXMiOnsidXNlcl9hZ2VudCI6IiIsImlwX2FkZHJlc3MiOiIifSwiYXV0aGVudGljYXRpb25fZmFjdG9ycyI6W3sidHlwZSI6Im9hdXRoIiwiZGVsaXZlcnlfbWV0aG9kIjoib2F1dGhfZ29vZ2xlIiwibGFzdF9hdXRoZW50aWNhdGVkX2F0IjoiMjAyNC0wOC0yNFQyMTo0NjoxMVoiLCJnb29nbGVfb2F1dGhfZmFjdG9yIjp7ImlkIjoib2F1dGgtdXNlci1saXZlLTM4Nzc0MGZiLWY3NzYtNGM3YS1iNzMyLTg1YjQxZDgyMDhlNSIsInByb3ZpZGVyX3N1YmplY3QiOiIxMTQ1NDI5Nzc3ODc0OTI4MTQzNjkifX1dfSwiaWF0IjoxNzI0NTM4NjIyLCJpc3MiOiJzdHl0Y2guY29tL3Byb2plY3QtbGl2ZS1kZGM3MTQ0ZS0xNjE2LTQ2MzMtYjA1OC01MTYzOTNlZTBlMTUiLCJuYmYiOjE3MjQ1Mzg2MjIsInN1YiI6InVzZXItbGl2ZS1mZmM1YjZjMS01ZDA2LTQ1ZjItYWZiNy01NWNiOTNkMmVhMGUifQ.wWSOHn731exxqxBW3w5qERfoiPLY0I-WkudbmNOOtn3qXUfObniJakBv0zPYmE2MwnZVPCbSS-_AK3klAgeIar-EaGqrMPa1BBfGPrSGc2S5FOr151iUDWojZ3q0AJ6LdsPCdaMDnlKJYBRzI4SHItH7ngdA1RGy_WmEEw_8HBzN5aT4CZTvc5y9EFnumSmVptTNQc635Xp_NCzHrJLlU7q3TwN11C_89lKP2-rQzqffX7Qw-qFMEGIEwU2kcZa4GHh80w-bt6eSA_WlSiW1mXJkldmvft17qqS23lEwnx0o8VyJBXAKBwXkQsYwS24gFFlJ8v0iPHD6MhUpVj7upQ",
    "content-length":
    "3426",
    "content-type":
    "application/json",
    "groq-app":
    "chat",
    "groq-organization":
    "org_01j635nschekj9q4p1geh6yzq7",
    "origin":
    "https://chat.groq.com",
    "priority":
    "u=1, i",
    "referer":
    "https://chat.groq.com/",
    "sec-ch-ua":
    '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile":
    "?0",
    "sec-ch-ua-platform":
    '"Windows"',
    "sec-fetch-dest":
    "empty",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-site":
    "same-site",
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-groq-keep-alive-pings":
    "true",
    "x-stainless-arch":
    "unknown",
    "x-stainless-lang":
    "js",
    "x-stainless-os":
    "Unknown",
    "x-stainless-package-version":
    "0.4.0",
    "x-stainless-runtime":
    "browser:chrome",
    "x-stainless-runtime-version":
    "128.0.0",
}

resp = requests.post("https://web.stytch.com/sdk/v1/sessions/authenticate",
    headers={
        'accept':
        '*/*',
        'accept-encoding':
        'gzip, deflate, br, zstd',
        'accept-language':
        'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'authorization':
        'Basic cHVibGljLXRva2VuLWxpdmUtMjZhODlmNTktMDlmOC00OGJlLTkxZmYtY2U3MGU2MDAwY2I1OmJPek5WU3RsWHJNcFhrbEFzaXNhTl9CeGhrVTZQZmNxWnNTbWxIb2djeXZy',
        'content-length':
        '2',
        'content-type':
        'application/json',
        'origin':
        'https://chat.groq.com',
        'priority':
        'u=1, i',
        'referer':
        'https://chat.groq.com/',
        'sec-ch-ua':
        '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'cross-site',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-sdk-client':
        'eyJldmVudF9pZCI6ImV2ZW50LWlkLTAxOTcwZGJhLTg2N2EtNDYxOS1hZDJlLWMzNTdjZTI0ZjE1ZiIsImFwcF9zZXNzaW9uX2lkIjoiYXBwLXNlc3Npb24taWQtZjFkZmExZmEtYTE5NC00NjBlLWE0MGYtYWQzYTVhMTdhYmE1IiwicGVyc2lzdGVudF9pZCI6InBlcnNpc3RlbnQtaWQtMGM2ZTUwZWYtZjkyNy00OTUyLTg4NGYtYmE2NjAwYWEzY2M0IiwiY2xpZW50X3NlbnRfYXQiOiIyMDI0LTA4LTI0VDIyOjUzOjM3LjU3NloiLCJ0aW1lem9uZSI6IkFtZXJpY2EvTmV3X1lvcmsiLCJzdHl0Y2hfdXNlcl9pZCI6InVzZXItbGl2ZS1mZmM1YjZjMS01ZDA2LTQ1ZjItYWZiNy01NWNiOTNkMmVhMGUiLCJzdHl0Y2hfc2Vzc2lvbl9pZCI6InNlc3Npb24tbGl2ZS1hNTVjMjYzYi1jNTY4LTQ4ZDQtOTMzYS1hYmY1OGQ3MGE5YTEiLCJhcHAiOnsiaWRlbnRpZmllciI6ImNoYXQuZ3JvcS5jb20ifSwic2RrIjp7ImlkZW50aWZpZXIiOiJTdHl0Y2guanMgSmF2YXNjcmlwdCBTREsiLCJ2ZXJzaW9uIjoiNC42LjAifX0=',
        'x-sdk-parent-host':
        'https://chat.groq.com'
    }
)
print(resp.status_code)
# print(resp.json())

# resp = requests.get("https://api.groq.com/openai/v1/models")
# print(resp.json())

# headers["authorization"] = "Bearer " + """
# eyJhbGciOiJSUzI1NiIsImtpZCI6Imp3ay1saXZlLTEyYTkzYTc0LWE3MWItNDJlMi1hODJiLTVjZTIyNjkxYTZkZSIsInR5cCI6IkpXVCJ9
# """.replace("\n","")
# resp = requests.post("https://api.groq.com/openai/v1/chat/completions",
#     headers = headers,
#     json={
#         "model": "llama3-8b-8192",
#         "messages": [
#             {
#             "content": "Please try to provide useful, helpful and actionable answers.",
#             "role": "system"
#             },
#             {
#             "content": "Clean up this sentance for me\n\n\"I go park yesterday\"\n\nreturn that sentance in json with the keys \"old\", \"new\", \"feedback\"\nMUST return json\nMUST give your feedback in the \"feedback\" key",
#             "role": "user"
#             },
#         ],
#         "temperature": 0.2,
#         "max_tokens": 2048,
#         "top_p": 1,
#         "stream": True
#     }
# )
# print(resp.cookies)
# print("\n")
# data = resp.text
# print(data)