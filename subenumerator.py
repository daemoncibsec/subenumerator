import httpx
import argparse

parser = argparse.ArgumentParser(
        prog='subnumerator',
        description='A tool to enumerate subdomain responses to HTTP(S) requests',
        epilog='Thanks for supporting me!',
        formatter_class=argparse.RawTextHelpFormatter
        )

parser.add_argument('file')
parser.add_argument('-s', '--https', action='store_true', help='Make the requests use HTTPS instead of the standard HTTP')
parser.add_argument('-o', '--output', help='Write the output inside a .txt file (must write the name of the file)')
parser.add_argument('-t', '--timeout', default=2 , help='Set the timeout value in seconds for the request. Default = 2')
args = parser.parse_args()

if not args.file:
    parser.error(f"No input provided. You must specify the file containing the subdomains which responses you want to enumerate.")

strtimeout = f'{args.timeout}.0'
timeout = float(strtimeout)
response_list = []

try:
    with open(f'{args.file}','r', encoding='utf-8') as file:
        counter=1
        print(f"Please consider supporting me on:\nGitHub - daemoncibsec | Instagram - @daemoncibsec")
        print("Starting the accessibility scan for the enumerated subdomains.")
        print(f'Nº\tStatus\t\t\t\tSubdomain')
        print('------------------------------------------------------------------')
        for line in file:
            url=line.strip()
            try:
                if args.https:
                    r = httpx.get(f"https://{url}/", timeout=timeout)
                else:
                    r = httpx.get(f"http://{url}/", timeout=timeout)
                print(f"{counter}\t[{r.status_code}]\t\t\t\t{url}")
                if args.output:
                    response_list.append(f"{counter}\t[{r.status_code}]\t\t\t\t{url}")
            except httpx.TimeoutException:
                print(f"{counter}\tTimeout reached\t\t\t{url}")
                if args.output:
                    response_list.append(f"{counter}\tTimeout reached\t\t\t{url}")
            except httpx.HTTPStatusError:
                print('{counter}\t{r.status_code}\t\t\t{url}')
                if args.output:
                    response_list.append(f"{counter}\t{r.status_code}\t\t\t\t{url}")
            except httpx.RequestError as e:
                if "No address associated with hostname" in str(e):
                    print(f"{counter}\tNo hostname associated\t\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\tNo hostname associated\t\t{url}")
                elif "Name or service not known" in str(e):
                    print(f"{counter}\tName or service not known\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\tName or service not known\t{url}")
                elif "Connection refused" in str(e):
                    print(f"{counter}\tConnection refused\t\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\tConnection refused\t\t{url}")
                elif "SSL: CERTIFICATE_VERIFY_FAILED" in str(e):
                    print(f"{counter}\tCertificate verification failed\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\tCertificate verification failed\t{url}")
                elif "Network is unreachable" in str(e):
                    print(f"{counter}\tNetwork is unreachable\t\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\tNetwork is unreachable\t\t{url}")
                elif "SSLV3_ALERT_HANDSHAKE_FAILURE" in str(e):
                    print(f"{counter}\tSSL handshake failed\t\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\tSSL handshake failed\t\t{url}")
                elif "Connection reset by peer" in str(e):
                    print(f"{counter}\tConnection reset by peer\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\tSSL handshake failed\t\t{url}")
                elif "Temporary failure in name resolution" in str(e):
                    print(f"{counter}\tName resolution failure\t\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\tTemporary failure in name resolution\t\t{url}")
                elif "tlsv1 alert internal error" in str(e):
                    print(f"{counter}\tTLSv1 alert internal error\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\tTLSv1 alert internal error\t{url}")
                else:
                    print(f"{counter}\t{e}\t\t\t{url}")
                    if args.output:
                        response_list.append(f"{counter}\t{e}\t\t\t{url}")
            counter+=1
except Exception as e:
    print(f'Execution error: {e}')

if args.output:
    try:
        if len(response_list) > 0:
            with open(f'{args.output}','w+', encoding='utf-8') as result:
                result.write("Please consider supporting me on:\nGitHub - daemoncibsec | Instagram - @daemoncibsec\nStarting the accessibility scan for the enumerated subdomains.\nNº\tStatus\t\t\t\tSubdomain\n------------------------------------------------------------------\n")
                for entry in response_list:
                    result.write(f'{entry}\n')
    except Exception as e:
        print(f'Execution error: {e}')
