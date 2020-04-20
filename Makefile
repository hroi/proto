all: build

build: build-go

build-go:
	protoc --go_out=paths=source_relative:. -I. *.proto */*.proto

clean:
	find . -name '*.pb.go' -delete
