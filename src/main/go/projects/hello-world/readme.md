## Project Setup

#### Hello World
```shell
asdf local golang 1.21.5
go mod init main
go run .
```

```shell
go get github.com/aws/aws-lambda-go/lambda
```

```shell
# remove download modules
go clean -modcache

# reinstall dependencies
go mod tidy
```

##### Lambda Function Config
- name: test-hello-go
- runtime: Amazon Linux 2023
- architecture: arm64
- handler: bootstrap


#### Links
- https://go.dev/doc/tutorial/getting-started
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-golang.html
- https://docs.aws.amazon.com/lambda/latest/dg/golang-handler.html
- https://github.com/aws-samples/sessions-with-aws-sam/tree/master/go-al2
- https://go.dev/doc/tutorial/web-service-gin
- https://community.aws/tutorials/golang-and-aws-lambda/02-golang-gin-app-on-aws-lambda

#### Potential Next Step Links
- https://github.com/gofiber/recipes
- https://www.reddit.com/r/golang/comments/10fy9ju/fastapi_replacement_especially_with_openapi/
- https://huma.rocks
- https://github.com/swaggest/rest
- https://github.com/emicklei/go-restful