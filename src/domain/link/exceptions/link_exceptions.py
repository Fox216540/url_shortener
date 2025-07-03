from src.core.exceptions.exception import Error

LAYER = "Domain/Link"

class LinkException(Error):
	def __init__(self, layer:str, message:str, error:str):
		message = f"Domain: Link\nLayer: {layer}\nMessage: {message}\nError: {error}"
		super().__init__(message)

class LinkServerException(LinkException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Server Error")


class InvalidCreateLink(LinkServerException):
	"""Invalid Create Link"""
	...

class InvalidCheckShortCode(LinkServerException):
	"""Invalid Check Short Code"""
	...

class InvalidGetLink(LinkServerException):
	"""Invalid Get Link"""
	...

class InvalidGetAllLinks(LinkServerException):
	"""Invalid Get All Links"""
	...

class InvalidDeleteLink(LinkServerException):
	"""Invalid Delete Link"""
	...

class InvalidDeleteAllLinks(LinkServerException):
	"""Invalid Delete All Links"""
	...

class LinkNotFoundException(LinkException):
	def __init__(self, layer:str, message:str):
		super().__init__(layer=layer, message=message, error="Not Found Error")

class LinkNotExists(LinkNotFoundException):
	"""Link Doesn't Exist"""
	...

class LinksNotExist(LinkNotFoundException):
	"""Links Don't Exist"""
	...

class LinkAlreadyExists(LinkNotFoundException):
	"""Link Already Exist"""
	...

class RoomOfLinkNotExists(LinkNotFoundException):
	def __init__(self):
		super().__init__(layer=LAYER, message="Room of Link Not Found")
