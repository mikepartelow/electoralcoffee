## Build Image

    docker build -t victorycoffee-build .

## Run Container

    docker run --rm -v`pwd`/app:/app -ti victorycoffee-build && cp -v app/html/index.html ../index.html