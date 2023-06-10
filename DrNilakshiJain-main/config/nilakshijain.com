server {
	server_name mail.nilakshijain.com;
	listen 443 ssl;
	ssl_certificate /etc/letsencrypt/live/mail.nilakshijain.com/fullchain.pem; # managed by Certbot
	ssl_certificate_key /etc/letsencrypt/live/mail.nilakshijain.com/privkey.pem; # managed by Certbot
	proxy_buffer_size 128k;
	proxy_buffers 64 512k;
	proxy_busy_buffers_size 512k;

	location / {	
		proxy_pass https://localhost:8443;
		proxy_set_header Host $http_host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
		proxy_connect_timeout 75;
		proxy_send_timeout 3650;
		proxy_read_timeout 3650;
		proxy_buffers 64 512k;
		client_body_buffer_size 512k;
		client_max_body_size 0;
	}
}
server {
	server_name mail.nilakshijain.com;
	listen 80;
    return 301 https://mail.nilakshijain.com$request_uri;
}

