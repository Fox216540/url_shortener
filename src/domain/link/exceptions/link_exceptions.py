from src.core.exceptions.exception import Error

class LinkException(Error):
	def __init__(self, layer:str, message:str):
		message = f"Domain: Link\nLayer: {layer}\nMessage: {message}"
		super().__init__(message)


class InvalidCreateLink(LinkException):
	"""Invalid Create Link"""
	...

class InvalidCheckShortCode(LinkException):
	"""Invalid Check Short Code"""
	...

class InvalidGetLink(LinkException):
	"""Invalid Get Link"""
	...

class InvalidGetAllLinks(LinkException):
	"""Invalid Get All Links"""
	...

class InvalidDeleteLink(LinkException):
	"""Invalid Delete Link"""
	...

class InvalidDeleteAllLinks(LinkException):
	"""Invalid Delete All Links"""
	...

class LinkNotExists(LinkException):
	"""Link Doesn't Exist"""
	...

class LinksNotExist(LinkException):
	"""Links Don't Exist"""
	...

