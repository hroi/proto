all: build

build: build-go build-ruby build-python
clean: clean-go clean-ruby clean-python

build-go:
	protoc --go_out=paths=source_relative:. -I. */*.proto
clean-go:
	find . -name '*.pb.go' -delete

build-ruby:
	protoc --ruby_out=. -I. */*.proto
clean-ruby:
	find . -name '*_pb.rb' -delete

build-python:
	protoc --python_out=. -I. */*.proto
clean-python:
	find . -name '*_pb2.py' -delete
