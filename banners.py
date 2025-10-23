BANNERS = {
    # -------------------------
    # DEFAULT
    # -------------------------
    "default": {
        "initial": b"login: ",
        "success": b"\r\nWelcome!\r\n",
        "prompt": b"> "
    },

    # -------------------------
    # TELNET / console (port 23)
    # -------------------------
    "telnet_ubuntu": {
        "initial": b"Ubuntu 22.04.3 LTS\nlogin: ",
        "success": b"\r\nWelcome to Ubuntu 22.04.3 LTS\r\n",
        "prompt": b"root@ubuntu:~# "
    },
    "telnet_debian": {
        "initial": b"Debian GNU/Linux 11 \nlogin: ",
        "success": b"\r\nAuthentication successful.\r\n",
        "prompt": b"root@debian:~# "
    },
    "telnet_busybox": {
        "initial": b"BusyBox v1.31.1 (built-in shell)\nlogin: ",
        "success": b"\r\n#\r\n",
        "prompt": b"# "
    },

    # -------------------------
    # SSH (port 22)
    # -------------------------
    "ssh_openssh_8": {
        "initial": b"SSH-2.0-OpenSSH_8.4p1 Debian-5+deb11u1\r\n",
        "success": b"",
        "prompt": b""
    },
    "ssh_dropbear": {
        "initial": b"SSH-2.0-dropbear_2018.76\r\n",
        "success": b"",
        "prompt": b""
    },

    # -------------------------
    # FTP (port 21)
    # -------------------------
    "ftp_vsftpd": {
        "initial": b"220 (vsFTPd 3.0.3)\r\n",
        "success": b"331 Please specify the password.\r\n",
        "prompt": b"230 Login successful.\r\n"
    },
    "ftp_proftpd": {
        "initial": b"220 ProFTPD Server (Debian)\r\n",
        "success": b"331 Password required for user.\r\n",
        "prompt": b"230 User logged in, proceed.\r\n"
    },

    # -------------------------
    # HTTP (porta 80) — respostas simples
    # -------------------------
    "http_apache": {
        "initial": b"HTTP/1.1 200 OK\r\nServer: Apache/2.4.41 (Ubuntu)\r\nContent-Type: text/html\r\n\r\n",
        "success": b"<html><body><h1>It works!</h1></body></html>\r\n",
        "prompt": b""
    },
    "http_nginx": {
        "initial": b"HTTP/1.1 200 OK\r\nServer: nginx/1.18.0 (Ubuntu)\r\nContent-Type: text/html\r\n\r\n",
        "success": b"<html><body><h1>Welcome to nginx!</h1></body></html>\r\n",
        "prompt": b""
    },

    # -------------------------
    # SMTP (porta 25)
    # -------------------------
    "smtp_postfix": {
        "initial": b"220 mail.example.com ESMTP Postfix\r\n",
        "success": b"250 OK\r\n",
        "prompt": b""
    },

    # -------------------------
    # BANCO DE DADOS / CACHE (handshakes simplificados)
    # -------------------------
    # MySQL (simplified)
    "mysql_5_7": {
        "initial": b"\x00\x00\x00\x2a5.7.33-log\x00",  # simplificação: parte do greeting
        "success": b"",
        "prompt": b""
    },
    # PostgreSQL (placeholder)
    "postgresql": {
        "initial": b"POSTGRESQL\r\n",  # simplificação — real é binário
        "success": b"",
        "prompt": b""
    },
    # Redis (simples)
    "redis": {
        "initial": b"+PONG\r\n",
        "success": b"+OK\r\n",
        "prompt": b""
    },

    # -------------------------
    # ROTEADORES / FIREWALLS (telnet/console-like)
    # -------------------------
    "cisco_ios": {
        "initial": b"User Access Verification\n\nUsername: ",
        "success": b"\r\nRouter> ",
        "prompt": b"Router> "
    },
    "juniper_junos": {
        "initial": b"login: \n\nWelcome to Juniper Networks Junos\n",
        "success": b"\r\nuser@host> ",
        "prompt": b"user@host> "
    },
    "mikrotik": {
        "initial": b"MikroTik RouterOS 6.45.9 (c) 1999-2019\nLogin: ",
        "success": b"\r\n[admin@MikroTik] > ",
        "prompt": b"[admin@MikroTik] > "
    },

    # -------------------------
    # IoT / embedded (comuns em scans)
    # -------------------------
    "dvr_busybox": {
        "initial": b"BusyBox v1.20.2 built-in shell (ash)\nLogin: ",
        "success": b"\r\n# ",
        "prompt": b"# "
    },

    # -------------------------
    # WINDOWS FTP (IIS)
    # -------------------------
    "ftp_windows_iis": {
        "initial": b"220 Microsoft FTP Service\r\n",
        "success": b"331 Password required for user\r\n",
        "prompt": b"230 User logged in.\r\n"
    }
}