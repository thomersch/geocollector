#!/usr/bin/env python

import logging
from web import http

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	logger = logging.getLogger(__name__)
	logger.info("Booting geolector")

	http.boot()