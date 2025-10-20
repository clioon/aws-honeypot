BANNERS = {
    "default": b"login: ",
    # -------------------------
    # Telnet / console / login
    # -------------------------
    "telnet_default": b"login: ",  # prompt genérico de login
    "telnet_ubuntu": b"Ubuntu 22.04.3 LTS\nlogin: ",  # Ubuntu console style
    "telnet_debian": b"Debian GNU/Linux 11 \nlogin: ",  # Debian-like
    "telnet_centos": b"CentOS Linux 7 (Core)\nlogin: ",  # CentOS prompt
    "telnet_busybox": b"BusyBox v1.31.1 (Ubuntu 1:1.31.1-1ubuntu1) built-in shell (ash)\nlogin: ",  # BusyBox shell
    "telnet_freebsd": b"FreeBSD 13.0-RELEASE\nlogin: ",  # FreeBSD banner
    "telnet_openbsd": b"OpenBSD 6.9 (GENERIC)\nlogin: ",  # OpenBSD banner
    "telnet_prompt_crlf": b"login: \r\n",  # prompt com CRLF

    # -------------------------
    # SSH protocol banners
    # -------------------------
    "ssh_openssh_7_6": b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3\r\n",
    "ssh_openssh_8_2": b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n",
    "ssh_openssh_latest": b"SSH-2.0-OpenSSH_9.0p1 Debian-0+deb11u1\r\n",
    "ssh_dropbear": b"SSH-2.0-dropbear_2018.76\r\n",
    "ssh_libssh": b"SSH-2.0-libssh-0.8.7\r\n",
    "ssh_generic": b"SSH-2.0-OpenSSH_8.4\r\n",
    "ssh_banner_custom": b"SSH-2.0-OpenSSH_7.9p1 MyCustomHost_1.0\r\n",

    # -------------------------
    # FTP / FTPS / vsftpd / proftpd / pure-ftpd
    # -------------------------
    "ftp_vsftpd_3_0_3": b"220 (vsFTPd 3.0.3)\r\n",
    "ftp_proftpd": b"220 ProFTPD Server (Debian) [::ffff:127.0.0.1]\r\n",
    "ftp_pureftpd": b"220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\r\n",
    "ftp_generic": b"220 Service ready for new user.\r\n",
    "ftp_windows_iis": b"220 Microsoft FTP Service\r\n",

    # -------------------------
    # SMTP / mail servers
    # -------------------------
    "smtp_postfix": b"220 mail.example.com ESMTP Postfix\r\n",
    "smtp_exim": b"220 smtp.example.com ESMTP Exim 4.92 #2 Fri, 01 Jan 2021 00:00:00 +0000\r\n",
    "smtp_sendmail": b"220 mail.example.com ESMTP Sendmail 8.14.4/8.14.4; Fri, 01 Jan 2021 00:00:00 +0000\r\n",

    # -------------------------
    # HTTP minimal responses (úteis para honeypots HTTP)
    # -------------------------
    "http_apache": b"HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\nContent-Type: text/html\r\n\r\n",
    "http_nginx": b"HTTP/1.1 200 OK\r\nServer: nginx/1.18.0 (Ubuntu)\r\nContent-Type: text/html\r\n\r\n",
    "http_iis": b"HTTP/1.1 200 OK\r\nServer: Microsoft-IIS/10.0\r\nContent-Type: text/html\r\n\r\n",

    # -------------------------
    # Routers / Switches / Network appliances
    # -------------------------
    "cisco_ios_15": (
        b"Cisco IOS Software, C2900 Software (C2900-UNIVERSALK9-M), Version 15.6(3)M2\n"
        b"Copyright (c) 1986-2016 by Cisco Systems, Inc.\n\nRouter> "
    ),
    "cisco_router": b"User Access Verification\n\nUsername: ",  # prompt de acesso (ex.: IOS/ASA style)
    "cisco_asav": b"ASA Version 9.8(2)\n\nType help or '?' for more information.\n\nUsername: ",
    "juniper_junos": b"login: \n\nWelcome to Juniper Networks Junos\n",
    "mikrotik_routeros": b"MikroTik RouterOS 6.45.9 (c) 1999-2019\nLogin: ",
    "ubiquiti_edgeos": b"EdgeOS v1.10.0\nlogin: ",
    "hp_procurve": b"HP Switch 2920-24G\n\nUsername:", 
    "brocade": b"Brocade Fabric OS\r\nlogin: ",
    "fortinet_fortios": b"FortiGate-VM64 #\n\nUsername: ",
    "huawei_vrp": b"Huawei Versatile Routing Platform (VRP)\nlogin: ",

    # -------------------------
    # Security devices / Firewalls / VPNs
    # -------------------------
    "paloalto": b"PA-VM login: ",
    "checkpoint": b"CPM login: ",
    "sonicwall": b"SonicWALL login: ",

    # -------------------------
    # Common Unix-like MOTD / welcome messages
    # -------------------------
    "motd_debian": (
        b"Debian GNU/Linux 11 \n\nThe programs included with the Debian GNU/Linux system are free software;\n"
    ),
    "motd_ubuntu_welcome": b"Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.4.0-xxx x86_64)\n\n",
    "motd_generic": b"Welcome to host.example.com\nLast login: Fri Jan  1 00:00:00 2021 from 1.2.3.4\n\nlogin: ",

    # -------------------------
    # IoT / embedded / camera / DVR
    # -------------------------
    "dvr_generic": b"BusyBox v1.20.2 (2012-08-02 11:17:02 CST) built-in shell (ash)\nLogin: ",
    "camera_onvif": b"HTTP/1.1 200 OK\r\nServer: ONVIF/2.0\r\n\r\n",
    "tplink_router": b"TP-Link Router (Archer) login: ",
    "dlink_router": b"D-Link Router\r\nLogin: ",

    # -------------------------
    # Misc / vendor OS prompts
    # -------------------------
    "telnet_solaris": b"SunOS 5.11\nlogin: ",
    "oracle_oss": b"Oracle Solaris 11.4\nlogin: ",
}