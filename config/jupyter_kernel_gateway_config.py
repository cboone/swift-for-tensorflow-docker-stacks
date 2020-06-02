# Configuration file for jupyter-kernel-gateway.

## IP address on which to listen (KG_IP env var)
c.KernelGatewayApp.ip = '0.0.0.0'

## Port on which to listen (KG_PORT env var)
c.KernelGatewayApp.port = 9999

## Permits listing of the running kernels using API endpoints /api/kernels and
#  /api/sessions (KG_LIST_KERNELS env var). Note: Jupyter Notebook allows this by
#  default but kernel gateway does not.
c.JupyterWebsocketPersonality.list_kernels = True
