"""
Proxy Pattern Implementation

Description:
Welcome to the "Proxy Pattern Implementation" module. This module explores and demonstrates the Proxy design pattern, 
a structural pattern in software design. The Proxy pattern provides a surrogate or placeholder for another object to control access to it. 
It is used when you want to add an additional level of control, such as lazy initialization, access control, or logging, to an object.

Module Overview:
- Problem Description: 
    We will start by presenting a scenario where direct access to an object may not be desirable due to various reasons, 
    and we need to introduce a proxy to control access.

- Solving with Proxy Pattern: 
    Next, we will implement the Proxy pattern to address the issues outlined in the problem description. 
    The Proxy will help us manage access to the real object, providing additional functionality or restrictions when needed.

By the end of this module, you will have a clear understanding of how to use the Proxy pattern to control and manage access to objects, 
improving security, performance, and resource management in your software systems.
"""

#Problem Scenario 1: Web Server Proxy (Like Nginx)

# Problem Description:
# Imagine you're building a web server to handle incoming HTTP requests. 
# Handling requests directly can be resource-intensive, and you need a way to improve performance and security. 
# You want to implement a proxy server, similar to Nginx, to manage access to your web server and provide features 
# like load balancing, caching, and access control.

# Solving with Proxy Pattern:

# 1. Create a WebServer class that represents the real server.
# 2. Implement a WebServerProxy class as the proxy, controlling access to the real server.
# 3. The proxy can perform tasks like load balancing, caching, and access control before passing requests to the real server.
# 4. Clients access the web server through the proxy, which ensures efficient and secure handling of requests.
from abc import ABC, abstractmethod

class IWebServer(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

# Real Subject: WebServer
class WebServer(IWebServer):
    def handle_request(self, request):
        # Process the HTTP request
        return f"Handling request: {request}"

# Proxy: WebServerProxy
class WebServerProxy(IWebServer):
    def __init__(self):
        self._web_server = WebServer()

    def handle_request(self, request):
        # Implement proxy functionality (e.g., load balancing, caching, access control)
        if request.startswith("/admin/"):
            return "Access denied"
        return self._web_server.handle_request(request)




# Problem Scenario 2: SMS Rate Limiter

# Problem Description:
# In a messaging application, you want to prevent users from sending too many SMS messages in a short period. 
# This is necessary to avoid spamming and to control system resources. 
# You need a solution to limit the rate at which users can send SMS messages.

# Solving with Proxy Pattern:

# 1. Create an SmsService class that represents the real SMS service.
# 2. Implement an SmsRateLimiter class as the proxy, controlling access to the real SMS service.
# 3. The proxy can track and limit the rate of SMS messages sent by each user.
# 4. Users send SMS messages through the proxy, which enforces rate limits and ensures fair usage.

class ISmsService(ABC):
    @abstractmethod
    def send_sms(self, user, message):
        pass

# Real Subject: SmsService
class SmsService(ISmsService):
    def send_sms(self, user, message):
        # Send SMS to the user
        return f"Sent SMS to {user}: {message}"

# Proxy: SmsRateLimiter
class SmsRateLimiter(ISmsService):
    def __init__(self, sms_service, rate_limit):
        self._sms_service = sms_service
        self._rate_limit = rate_limit
        self._usage = {}

    def send_sms(self, user, message):
        # Implement rate limiting logic
        if user not in self._usage:
            self._usage[user] = 0
        if self._usage[user] < self._rate_limit:
            self._usage[user] += 1
            return self._sms_service.send_sms(user, message)
        else:
            return "Rate limit exceeded"

# Client
if __name__ == "__main__":
    print("================== Start of Web Server Example ==================")
    proxy = WebServerProxy()
    request1 = "/home"
    request2 = "/admin/sensitive-data"

    response1 = proxy.handle_request(request1)
    response2 = proxy.handle_request(request2)

    print(response1)  # Output: Handling request: /home
    print(response2)  # Output: Access denied
    
    print("================== End of Web Server Example ==================")
    print("================== Start of SMS Limiter Example ==================")
    
    
    
    sms_service = SmsService()
    rate_limited_service = SmsRateLimiter(sms_service, rate_limit=3)

    user1 = "Alice"
    user2 = "Bob"

    response1 = rate_limited_service.send_sms(user1, "Hello, Alice!")
    response2 = rate_limited_service.send_sms(user1, "Message 2")
    response3 = rate_limited_service.send_sms(user1, "Message 3")
    response4 = rate_limited_service.send_sms(user1, "Message 4")
    response5 = rate_limited_service.send_sms(user2, "Hello, Bob!")

    print(response1)  # Output: Sent SMS to Alice: Hello, Alice!
    print(response2)  # Output: Sent SMS to Alice: Message 2
    print(response3)  # Output: Sent SMS to Alice: Message 3
    print(response4)  # Output: Rate limit exceeded
    print(response5)  # Output: Sent SMS to Bob: Hello, Bob!
    print("================== End of SMS Limiter Example ==================")
