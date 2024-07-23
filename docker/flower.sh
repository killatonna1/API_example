#!/bin/sh

celery --app=app.tasks.celery:celery_app flower