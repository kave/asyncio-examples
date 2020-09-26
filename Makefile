CIRCLE_BUILD_NUM ?= latest
image_name := qrcodes
gitsha := $(shell git rev-parse HEAD)

define build_image
docker build . \
	--tag $(image_name):$(CIRCLE_BUILD_NUM)
endef

define docker_run
docker run \
	-p 8000:8000 $(image_name):$(CIRCLE_BUILD_NUM)
endef

run-local:
	$(call docker_run)

image-latest:
	$(call build_image)

image: image-latest

run: run-local