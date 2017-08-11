MAKEFLAGS+=--no-print-directory
REDIS=$(shell which redis-cli)
REDIS_KEY="celery"
time=$(shell date +%s)
env=./.env
serviceName=test
api=

# gnu xargs only
# for mac. please install findutils
post:
	. $(env) && $(MAKE) sound  | \
		gxargs -iDECIBEL $(MAKE) service/metric size=DECIBEL api=$$MACKEREL_API_KEY

setup:
	cp -f .env.sample .env

sound:
	@echo $$RANDOM

service/metric:
	@curl "https://mackerel.io/api/v0/services/$(serviceName)/tsdb" \
		-X POST \
		--silent \
		--show-error \
		-d '[{"name":"celery_queue_size", "time": $(time), "value": $(size)}]' \
		-H 'Content-Type: application/json' \
		-H 'X-Api-Key: $(api)'
