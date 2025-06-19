from src.domain.link.exceptions.link_exceptions import *

ERRORS_SERVER = [
	InvalidCreateLink,
	InvalidCheckShortCode,
	InvalidDeleteLink,
	InvalidDeleteAllLinks,
	InvalidGetLink,
	InvalidGetAllLinks,
]

ERRORS_NOT_FOUND = [
	LinkNotExists,
	LinksNotExist,
]
ERRORS_LINK_REPO = ERRORS_SERVER + ERRORS_NOT_FOUND
