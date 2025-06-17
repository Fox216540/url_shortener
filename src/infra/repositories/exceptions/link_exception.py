from src.domain.link.exceptions.link_exceptions import LinkException

LAYER = "Infra/repositories/link"


class InvalidCreateLink(LinkException):
	"""Invalid Create Link"""
	message = "Invalid Create Link"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidCheckShortCode(LinkException):
	"""Invalid Check Short Code"""
	message = "Invalid Check Short Code"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidGetLink(LinkException):#get_by_alias
	"""Invalid Get Link"""
	message = "Invalid Get Link"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidGetAllLinks(LinkException):
	"""Invalid Get All Links"""
	message = "Invalid Get All Links"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidDeleteLink(LinkException):
	"""Invalid Delete Link"""
	message = "Invalid Delete Link"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InvalidDeleteAllLinks(LinkException):
	"""Invalid Delete All Links"""
	message = "Invalid Delete All Links"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class LinkNotExists(LinkException):
	"""Link Doesn't Exist"""
	message = "Link Doesn't Exist"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class LinksNotExist(LinkException):
	"""Links Don't Exist"""
	message = "Links Don't Exist"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


ERRORS_SERVER = [
	InvalidCreateLink,
	InvalidCheckShortCode,
	InvalidGetLink,
	InvalidGetAllLinks,
	InvalidDeleteLink,
	InvalidDeleteAllLinks,
]

ERRORS_NOT_FOUND = [
	LinkNotExists,
	LinksNotExist,
]

ERRORS_ALL = ERRORS_SERVER + ERRORS_NOT_FOUND