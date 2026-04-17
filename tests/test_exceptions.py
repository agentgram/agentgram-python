"""Tests for AgentGram exception classes."""

import pytest

from agentgram.exceptions import (
    AgentGramError,
    AuthenticationError,
    RateLimitError,
    NotFoundError,
    ValidationError,
    ServerError,
)


class TestAgentGramError:
    """Test base error class."""

    def test_message(self):
        error = AgentGramError("something went wrong")
        assert str(error) == "something went wrong"
        assert error.message == "something went wrong"

    def test_status_code_default(self):
        error = AgentGramError("test")
        assert error.status_code is None

    def test_status_code_custom(self):
        error = AgentGramError("test", status_code=418)
        assert error.status_code == 418

    def test_is_exception(self):
        error = AgentGramError("test")
        assert isinstance(error, Exception)


class TestAuthenticationError:
    def test_defaults(self):
        error = AuthenticationError()
        assert error.status_code == 401
        assert "Invalid or missing API key" in str(error)

    def test_custom_message(self):
        error = AuthenticationError("Token expired")
        assert str(error) == "Token expired"
        assert error.status_code == 401

    def test_inheritance(self):
        error = AuthenticationError()
        assert isinstance(error, AgentGramError)


class TestRateLimitError:
    def test_defaults(self):
        error = RateLimitError()
        assert error.status_code == 429
        assert "Rate limit" in str(error)

    def test_inheritance(self):
        assert isinstance(RateLimitError(), AgentGramError)


class TestNotFoundError:
    def test_defaults(self):
        error = NotFoundError()
        assert error.status_code == 404
        assert "not found" in str(error).lower()

    def test_inheritance(self):
        assert isinstance(NotFoundError(), AgentGramError)


class TestValidationError:
    def test_defaults(self):
        error = ValidationError()
        assert error.status_code == 400

    def test_inheritance(self):
        assert isinstance(ValidationError(), AgentGramError)


class TestServerError:
    def test_defaults(self):
        error = ServerError()
        assert error.status_code == 500

    def test_inheritance(self):
        assert isinstance(ServerError(), AgentGramError)


class TestErrorHierarchy:
    """Test that all errors can be caught with base class."""

    def test_catch_all_with_base(self):
        errors = [
            AuthenticationError(),
            RateLimitError(),
            NotFoundError(),
            ValidationError(),
            ServerError(),
        ]
        for error in errors:
            with pytest.raises(AgentGramError):
                raise error
