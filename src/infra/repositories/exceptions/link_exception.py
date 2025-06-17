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
	message = "Invalid Create Link"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidCheckShortCode(InvalidCheckShortCode):
	message = "Invalid Check Short Code"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidGetLink(InvalidGetLink):#get_by_alias
	message = "Invalid Get Link"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidGetAllLinks(InvalidGetAllLinks):
	message = "Invalid Get All Links"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidDeleteLink(InvalidDeleteLink):
	message = "Invalid Delete Link"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)


class InfraInvalidDeleteAllLinks(InvalidDeleteAllLinks):
	message = "Invalid Delete All Links"

	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraLinkNotExists(LinkNotExists):
	message = "Link Doesn't Exist"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

class InfraLinksNotExist(LinksNotExist):
	message = "Links Don't Exist"
	def __init__(self):
		super().__init__(layer=LAYER, message=self.message)

