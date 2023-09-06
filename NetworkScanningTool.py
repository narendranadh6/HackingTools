import nmap
import pandas as pd
class NetworkScanningTool:
    
    def scan(self,target_ip, target_ports):
        a=[]
        nm = nmap.PortScanner()
        scan_results = nm.scan(hosts=target_ip, arguments=f' -p {",".join(map(str, target_ports))}')
       
        for host, scan_result in scan_results['scan'].items():
            print(f"Scanning results for host: {host}")
            print("")
            for port, port_info in scan_result['tcp'].items():
                my_list=[]
                my_list.append(port)
                my_list.append(port_info['name'])
                my_list.append(port_info['state'])
                my_list.append(port_info['reason'])
                service = port_info.get('product', '') + " " + port_info.get('version', '')
                a.append(my_list)
        df = pd.DataFrame(a,columns=['Port','Port-name','Status','Reason'])
        print(df)
                
                


target_ip = input("Enter target ip :")  
target_ports = list(map(int,input("Enter ports you want to scan :").split())) 
network=NetworkScanningTool();
network.scan(target_ip, target_ports)
