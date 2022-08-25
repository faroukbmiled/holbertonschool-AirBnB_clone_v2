# task 0 redone with puppet.

$cfg = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

$nginx = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
}"

$dirs = [ '/data', '/data/web_static',
            '/data/web_static/releases', '/data/web_static/releases/test',
                '/data/web_static/shared',
                  ]

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

file { $dirs:
  ensure => 'directory'
} ->

exec { 'chown -R ubuntu:ubuntu /data':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $cfg
} ->

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx
} ->

exec { 'nginx restart':
  path => '/etc/init.d/'
}
