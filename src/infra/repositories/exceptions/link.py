from src.domain.link.exceptions.link_exceptions import LinkException

class InvalidCreateLink(LinkException):
	message = LinkException.message + "invalid create"