from src.domain.link.exceptions.link_exceptions import (
InvalidCreateLink,
InvalidCheckShortCode,
InvalidGetLink,
InvalidGetAllLinks,
InvalidDeleteLink,
InvalidDeleteAllLinks,
LinkNotExists,
LinksNotExist,
)

LAYER = "Infra/repositories/link"


class InfraInvalidCreateLink(InvalidCreateLink):
	"""Invalid Create Link"""
	message = "Invalid Create Link"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidCheckShortCode(InvalidCheckShortCode):
	"""Invalid Check Short Code"""
	message = "Invalid Check Short Code"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidGetLink(InvalidGetLink):#get_by_alias
	"""Invalid Get Link"""
	message = "Invalid Get Link"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidGetAllLinks(InvalidGetAllLinks):
	"""Invalid Get All Links"""
	message = "Invalid Get All Links"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidDeleteLink(InvalidDeleteLink):
	"""Invalid Delete Link"""
	message = "Invalid Delete Link"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidDeleteAllLinks(InvalidDeleteAllLinks):
	"""Invalid Delete All Links"""
	message = "Invalid Delete All Links"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraLinkNotExists(LinkNotExists):
	"""Link Doesn't Exist"""
	message = "Link Doesn't Exist"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraLinksNotExist(LinksNotExist):
	"""Links Don't Exist"""
	message = "Links Don't Exist"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

