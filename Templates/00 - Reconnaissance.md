### Information Gathering
**Operating-System:**
- 
**Web-Technology:**
_Content Management System/Backend Technology_
- 
**Hostname:**
- 
**Security Policy:**
- 
**Functionalities:**
- 
<%* 
let filename = tp.file.title;

if ( filename.startsWith("Untitled") ) {
  filename = tp.file.folder(true).split('/')[1];
  await tp.file.rename(filename);
  tp.file.move("01 - HackTheBox/"+filename+'/'+filename)
} 

await this.app.vault.createFolder("01 - HackTheBox/"+filename+"/Logs/");
await this.app.vault.createFolder("01 - HackTheBox/"+filename+"/Scripts/");
const address = await tp.system.prompt("Set the target address");
-%>
---
**Target Address**
```
<%address%>
```
### Network Scanning
- [i] The following command get the relevant information from logs
```bash
grep -P '^[A-Z]{4}|^[0-9]' Logs/all_ports_tcp.nmap | xclip -sel clip
```
#### Network Scanning TCP
- [ ] Nmap scanning TCP
```bash
sudo nmap -sCV -p- --open -vvv --min-rate=5000 <%address%> -oN Logs/all_ports_tcp.nmap
```
- Relevant information about scans
```

```
#### Network Scanning UDP
- [ ] Nmap scanning UDP
```bash
sudo nmap -sUV --top-ports 1000 -vvv <%address%> -oN Logs/udp_top_1000_ports.nmap
```
- Relevant information about scans
```

```

