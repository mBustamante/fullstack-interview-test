# Prendea API

## Use

### Development

Uses the default Django development server.

1. Create *.env* file with enviroment variables.
2. Install prerequisites:

    ```sh
    $ make install
    ```
3. Build the images:

    ```sh
    $ make build
    ```
4. Serve development server:

    ```sh
    $ make serve
    ```

Test it out at [http://localhost:9000](http://localhost:9000). The "app" folder is mounted into the container and code changes apply automatically.

Run zappa scripts:

    ```sh
    $ zappa invoke [stage:staging|production] 'module_route.script_name'
    ```

Connect mysql from any client to port 3307.