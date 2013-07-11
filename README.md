Burton
======

CLI-based web server control panel


FAQ
===

Why is a CLI-based server control panel called "Burton"?
--------------------------------------------------------

My original intention was to create a CLI-based Plesk replacement, or Clisk. However it turns out that the Clisk name was already taken, so I started to look for other words which start with the letters CLI.

Does Burton support XYZ Plesk feature?
--------------------------------------

Please check! The feature list is growing all the time. If Burton doesn't yet support the feature, then please file an issue, and carefully describe your use case and how you would expect it to work in a CLI environment. I'll try to get it coded.

Why is Burton free?
-------------------

Two reasons: 1) I benefit from the Open Source community, so I contribute back. 2) I want you to use it, so that you can help me find the missing features and add them!

Is Burton hacker-proof? Plesk is very insecure, does Burton suffer the same issues?
-----------------------------------------------------------------------------------

Burton is not hacker-proof, nor is it intended to be. When properly configured and maintained, your operating system and related components provide the best type of protection that you can have. Burton can only be operated on the CLI and is therefore only available to those who already have shell access. Furthermore, all of Burton's operations are done using conventional system calls, using your operating system's inherent security features. You must have root access to the server to perform most operations with Burton. Burton does not expose any features outside the CLI environment, and every operation that Burton performs is accomplished using standard OS tools. Therefore Burton introduces zero security risk to the system.

How can Burton be so secure, yet Plesk is so insecure?
------------------------------------------------------

Plesk and other web-based control panels suffer a fundamental flaw: they expose privileged configuration options to an unprivileged environment (the World Wide Web), then tack on their own 'privilege management' in the form of user accounts with passwords. Even when properly coded, Plesk will still suffer all the standard security issues inherent in web applications, such as Cross-Site Scripting, PHP and Apache vulnerabilities, browser vulnerabilities, etc. ad nauseum. Additionally, vulnerabilities in Plesk itself are well known and discovered on a regular basis. Burton is not exposed to an unprivileged environment, and thus does not present any new attack vectors.

Who finances Burton development?
--------------------------------

My employer! Burton started as a project to help myself and other admins manage our own servers without a web-based control panel. I generally add features as we need them in-house.

With which software is Burton compatible?
-----------------------------------------

New software support is easy to add to Burton. For the 1.0 release, I am aiming to support the software that I use at work: Ubuntu Server, Apache2, Postfix, Dovecot2, and Python3.

Will Burton work with my existing system setup?
-----------------------------------------------

1. For websites: If you are using Apache2 with the typical Ubuntu Server sites-available configuration, then yes.
2. For email, if you are using Postfix with Dovecot2, Maildir and passwd-file, then yes.


TODO
====

1. Check installed versions of software: apache2, dovecot2, postfix

License
=======

After consulting with the following license wizards:...
	http://www.openfoundry.org/LicenseWizard2EN/LicenseWizard.cgi
	http://home.ccil.org/~cowan/floss/
	http://www.oss-watch.ac.uk/apps/licdiff/
...I have decided to license Burton under the GNU General Public License v2.0.

If you would like to use Burton under a different software license you are encouraged to contact me and explain what you would like to do. I'm easy to get along with.

Copyright 2013, Dotan Cohen
http://dotancohen.com
