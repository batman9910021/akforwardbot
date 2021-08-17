#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    API_ID = int(os.environ.get("API_ID", 1477116))
    API_HASH = os.environ.get("API_HASH", "302d0ec70c1e2e29d6193c00c149e439")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1942867661:AAFFkFDvAwG4T2SSGwYcWFaVRrVvX8tUOUo") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@unigramappx")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "empty")
    OWNER_ID = os.environ.get("OWNER_ID", "991837880")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQAnbw7cfsJVD4-EkXQ0NzdIv66UCLw3uzTzPRvQb60ToRByYb3C3i6MyqC9PaflZnTCsTHWiyaNMokpUW8TUVxacs3MA_1QPq3ZJOO2qCmrVeyqVw51DQU8CPim9VLGpapfBrRPy7ea8V8GGs0x0aVhbV0tGsVmP8zmSVN_y_uWLKbnEm6BhV6a403U-JbHbVUvqmUsVIa-A5sYv9oPjJWgVVLhU-hPH-lL5u9h6DpPrJKMytOEpXDwqakDLKvCyAH-Q3ospfZJGCCiw_SjaOnzqJ7YLXYn360hcVnDm0kk8IPrfSxPypkW34V1LCJGWgQk1Mpls3QA6xXYe7TAr0ezOx4-uAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001567511355"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
