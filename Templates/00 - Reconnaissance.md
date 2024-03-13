**Operating-System:**
- 
**Web-Technology:**
_Content Management System/Backend Technology_
- 
**Hostname:**
- 
<%* 
let filename = tp.file.title;

if ( filename.startsWith("Untitled") ) {
  filename = await tp.system.prompt("File name: ");
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
#### Network Scanning TCP
- [ ] Nmap scanning TCP
```bash
sudo nmap -sCV -p- --open -vvv --min-rate=5000 <%address%> -oN logs/all_ports_tcp.nmap
```
- Relevant information about scans
```

```
#### Network Scanning UDP
- [ ] Nmap scanning UDP
```bash
sudo nmap -sUV --top-ports 1000 -vvv <%address%> -oN logs/udp_top_1000_ports.nmap
```
- Relevant information about scans
```

```