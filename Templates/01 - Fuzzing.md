### Directory Brute Forcing
<%* const address = await tp.system.prompt("Set the target address"); -%>
#### Raft medium word lowercase
- [ ] Fuzzing words
```bash
ffuf -u http://<%address%>/FUZZ -w $WEB_CONENT/raft-medium-words-lowercase.txt
```
- Relevant words found
```

```
#### Raft medium files lowercase
- [ ] Fuzzing files
```bash
ffuf -u http://<%address%>/FUZZ -w $WEB_CONENT/raft-medium-files.txt
```
- Relevant files found
```

```
#### Raft medium directories lowercase
- [ ] Fuzzing directories
```bash
ffuf -u http://<%address%>/FUZZ -w $WEB_CONENT/raft-medium-directories-lowercase.txt
```
- Relevant directories found
```

```

_Do not forget try with `-e .php,.bak,.log` and other dictionaries_