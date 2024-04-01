# Description

This repository contains templates for commonly used security autotests.

**Security autotests** - are automated tests that verify previously identified security issues and vulnerabilities. If you uncover a vulnerability and want to verify it automatically after developers have provided fixes, you can create a security auto-test in just a few clicks.

For quick creation of security auto-tests, you can use the Burp Suite + [Copy As Python-Requests](https://github.com/portswigger/copy-as-python-requests) extension + templates. 

This repository includes examples such as:
- base template
- input validation
- security headers validation
- rate limits validation
- user enumeration
- etc.

You can learn more about security autotests on our blog: https://www.cossacklabs.com/blog/ (link to be added later)

# Usage
1. Choose a vulnerability template.
2. Copy and paste the code into an IDE (or clone the repository).
3. Copy request(s) from Burp using the [Copy As Python-Requests](https://github.com/portswigger/copy-as-python-requests) extension.
4. Modify the template according to your needs. You can change the `MESSAGE` variable, `verification()` function, and any other necessary code.
5. *Optionally*, add a function to login into the tested application if future requests require session tokens.
6. Run the code and ensure it works correctly.
