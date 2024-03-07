from flask import Flask
from opcua import Client

app = Flask(__name__)

@app.route('/')
def read_opc_data():
    try:
        # Connect to Kepware OPC server
        opc_server_endpoint = "opc.tcp://192.168.103.13:4841/"
        client = Client(opc_server_endpoint)
        client.connect()
        print("Connected to OPC UA server")

        # OPC UA node information
        node_id = "ns=3;s=22092_20000.nsuri=OpcUaServer;s=Application.CSc_HMI.CSc_IO.dw_CounterPass"

        # Get the node using the complete node ID
        node = client.get_node(node_id)

        # Read data from OPC node
        data = node.get_value()

        # Disconnect from the OPC server
        client.disconnect()

        return {'The OPC Data that we get is': data}
    except Exception as e:
        return {'Error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)
