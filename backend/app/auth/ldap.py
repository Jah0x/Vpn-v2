"""Simple LDAP helper for interacting with GLAuth."""

import os
from typing import Optional

from ldap3 import Connection, Server, ALL
from ldap3.core.exceptions import LDAPSocketOpenError

GLAUTH_HOST = os.environ.get("GLAUTH_HOST", "localhost")
GLAUTH_PORT = int(os.environ.get("GLAUTH_PORT", 389))
GLAUTH_BIND_DN = os.environ.get("GLAUTH_BIND_DN", "cn=admin,dc=example,dc=com")
GLAUTH_BIND_PASSWORD = os.environ.get("GLAUTH_BIND_PASSWORD", "admin")
GLAUTH_BASE_DN = os.environ.get("GLAUTH_BASE_DN", "dc=example,dc=com")


class LDAPClient:
    """Lightweight wrapper around ldap3 for GLAuth operations."""

    def __init__(self) -> None:
        self.server = Server(GLAUTH_HOST, port=GLAUTH_PORT, get_info=ALL)
        try:
            self.conn = Connection(
                self.server,
                user=GLAUTH_BIND_DN,
                password=GLAUTH_BIND_PASSWORD,
                auto_bind=True,
            )
        except LDAPSocketOpenError:
            # Allow running without LDAP server, e.g. in tests
            self.conn = None

    def create_user(self, uid: str, email: str, password: str) -> bool:
        """Create a user entry in GLAuth."""

        if not self.conn:
            return False
        dn = f"uid={uid},{GLAUTH_BASE_DN}"
        attributes = {
            "objectClass": ["inetOrgPerson", "posixAccount"],
            "uid": uid,
            "sn": uid,
            "mail": email,
            "userPassword": password,
        }
        return self.conn.add(dn, attributes=attributes)

    def get_user(self, uid: str) -> Optional[dict]:
        """Retrieve a user entry."""

        if not self.conn:
            return None
        dn = f"uid={uid},{GLAUTH_BASE_DN}"
        if self.conn.search(dn, "(objectClass=*)", attributes=["mail"]):
            return self.conn.entries[0].entry_to_json()
        return None
