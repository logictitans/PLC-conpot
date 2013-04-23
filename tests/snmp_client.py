from pysnmp.entity import engine, config
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.entity.rfc3413 import cmdgen

import sys
sys.path.append('./')
import config as conpot_config


class SNMPClient(object):
    def __init__(self):
        # Create SNMP engine instance
        self.snmpEngine = engine.SnmpEngine()

        # user: usr-sha-aes, auth: SHA, priv AES
        config.addV3User(
            self.snmpEngine, 'usr-sha-aes128',
            config.usmHMACSHAAuthProtocol, 'authkey1',
            config.usmAesCfb128Protocol, 'privkey1'
        )
        config.addTargetParams(self.snmpEngine, 'my-creds', 'usr-sha-aes128', 'authPriv')

        # Setup transport endpoint and bind it with security settings yielding
        # a target name (choose one entry depending of the transport needed).

        # UDP/IPv4
        config.addSocketTransport(
            self.snmpEngine,
            udp.domainName,
            udp.UdpSocketTransport().openClientMode()
        )
        config.addTargetAddr(
            self.snmpEngine, 'my-router',
            udp.domainName, (conpot_config.snmp_host, conpot_config.snmp_port),
            'my-creds'
        )

    # Error/response receiver
    def cbFun(self, sendRequestHandle, errorIndication, errorStatus, errorIndex, varBindTable, cbCtx):
        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?')
            )
        else:
            for oid, val in varBindTable:
                print('%s = %s' % (oid.prettyPrint(), val.prettyPrint()))

    def get_command(self):
        # Prepare and send a request message
        cmdgen.GetCommandGenerator().sendReq(
            self.snmpEngine,
            'my-router',
            (((1, 3, 6, 1, 2, 1, 1, 1, 0), None), ),
            self.cbFun
        )

        # Run I/O dispatcher which would send pending queries and process responses
        self.snmpEngine.transportDispatcher.runDispatcher()


if __name__ == "__main__":
    snmp_client = SNMPClient()
    snmp_client.get_command()