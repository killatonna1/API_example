#!/bin/sh

celery --app=app.tasks.celery:celery_app worker -l INFO