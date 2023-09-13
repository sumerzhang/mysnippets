1. Install VS Code, the WSL extension, and the Mojo extension.
2. Install Ubuntu 22.04 for WSL and open it.
3. In the Ubuntu terminal, install the Modular CLI:
```shell
curl https://get.modular.com | \
  MODULAR_AUTH=mut_2dc30aa7773942b99f027f173b6a8610 \
  sh -
```
Command copied to clipboard
4. Install the Mojo SDK:
```shell
modular install mojo
```

5. Open the Ubuntu workspace in VS Code with this:

code .
Command copied to clipboard

6. Get started with Hello World!