# n8n

## How to Run

```bash
docker-compose -f docker-compose.yml --env-file .env up
```

## Customize image

### 1. Build your image from Dockerfile

```bash
docker build -t jasonlws/n8n:1.84.3 --build-arg IMAGE_NAME=n8nio/n8n --build-arg IMAGE_TAG=1.84.3 --no-cache .
```

### 2. Run it

#### Docker compose

```bash
docker-compose -f docker-compose.yml --env-file .env.jasonlws up
```

## License

MIT - a permissive free software license originating at the Massachusetts Institute of Technology (MIT), it puts only very limited restriction on reuse and has, therefore, an excellent license compatibility. It permits reuse within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.

Check the [LICENSE file](https://github.com/jasonlws/docker-library/blob/master/LICENSE) for more details.