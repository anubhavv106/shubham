# DrNilakshiJain

Hi, I'm Mustansir Godhrawala. I created and maintain this repository, below you can find how to make changes and edit the configuration for Nilakshi ma'am's website. 

### Implementation
1. Nginx- The web server used to serve the website on the origin server[techy name for my server essentially]. 
2. Cloudflare- The proxy used to cache and serve the static and html files from the website, incase of downtime or maintenance. Helps us use less bandwidth and serve the site faster and scale to millions of requests. 
3. Docker- The website is containerized for efficient serving, this allows anyone to push changes to this repository and trigger a docker image build which is then published to a private docker registry which then restarts the process using the new image. 
4. Reverse Proxy- Nginx reverse proxies the requests to docker containers which in turn serve the required web page. 
5. Django- We use django to serve and maintain ma'am's website, this gives her easy access to an admin console to add certifications and more. 
6. Gunicorn- This is the WSGI server we use to connect the docker network to django.

#### Email Implementation
The configuration for email works on dockerized mailcow, I backup the emails about once a month. Any emails you get here, I would be able to get access though, so this configuration is mostly there so I can connect it to your website. Mailcow is occasionally buggy and some mailservers are not able to send emails to it. 

### Passwords
1. Mail Admin
- Site: mail.nilakshijain.com
- Admin Username: nilakshijain
- Admin Password: #,IoNTerED,73
This access is domain specific, for admin related email settings please ping me. You can set most settings here though. 

2. Django Admin
- Site: nilakshijain.com/admin
- Admin Username: admin
- Admin Password: #,IoNTerED,73
This panel will allow you to add and remove objects/items from your website with ease, like add details about experience and certifications. 

3. Mailjet Relay
- Site: https://app.mailjet.com
- Admin Username: nilakshijain1986@gmail.com
- Admin Password: egfov6Osh{gleg
This relay will allow you send emails, it has a limit of 200 emails per day. If you try to send more it will bounce.





### How to add/remove stuff?
