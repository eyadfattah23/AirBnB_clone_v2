# Puppet manifest that sets up web servers for the deployment of web_static

# 1. Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# 2. Create the folder /data/web_static/releases/test and its parents if not already exist
file { '/data/web_static/releases/test':
  ensure => directory,
  mode   => '0755',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => Package['nginx'],
}

# 3. Create the folder /data/web_static/shared/ if it doesn’t already exist
file { '/data/web_static/shared':
  ensure => directory,
  mode   => '0755',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => Package['nginx'],
}

# 4. Create a fake HTML file (to test your Nginx configuration)
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Melius will be alive soon!!',
  mode    => '0644',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases/test'],
}

# 5. Create a symbolic link /data/web_static/current to the releases/test/
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => File['/data/web_static/releases/test'],
}

# 6. Give ownership of the /data/ folder to the ubuntu user AND group
file { '/data':
  ensure => directory,
  recurse => true,
  owner => 'ubuntu',
  group => 'ubuntu',
  require => [ File['/data/web_static/shared'], File['/data/web_static/releases/test'] ],
}

# 7. Update the Nginx configuration to serve the content
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# 8. Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}

# Template for Nginx configuration (nginx/default.erb)
# You need to create a template file for the Nginx configuration.
# Save the following content in the file modules/nginx/templates/default.erb:

# /etc/nginx/sites-available/default.erb
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}

# Ensure you have the necessary Puppet module structure and templates in place.
# This example assumes the existence of a 'nginx' module with the template stored at
# modules/nginx/templates/default.erb.
