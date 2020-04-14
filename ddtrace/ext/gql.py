from contextvars import ContextVar

RESOLVER_NAME: ContextVar[str] = ContextVar("resolver_name", default=None)
