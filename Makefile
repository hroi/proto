PROTO_FILES=$(shell find . -name *.proto -depth +1)
all: build

build: build-go build-ruby build-python
clean: clean-go clean-ruby clean-python

build-go:
	protoc --go_out=paths=source_relative:. -I. ${PROTO_FILES}
clean-go:
	find . -name '*.pb.go' -delete

build-ruby:
	protoc --ruby_out=. -I. ${PROTO_FILES}
clean-ruby:
	find . -name '*_pb.rb' -delete

build-python:
	protoc --python_out=. -I. ${PROTO_FILES}
clean-python:
	find . -name '*_pb2.py' -delete
