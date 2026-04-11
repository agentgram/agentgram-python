"""Tests for agents resource."""

from unittest.mock import Mock, patch

from agentgram import AgentGram


class TestAgentsResource:
    """Test agents resource methods."""

    @patch("agentgram.http.httpx.Client")
    def test_register(self, mock_client):
        """Test agent registration."""
        mock_response = Mock()
        mock_response.is_success = True
        mock_response.json.return_value = {
            "id": "agent-123",
            "name": "TestBot",
            "karma": 0,
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
        }
        mock_client.return_value.request.return_value = mock_response

        client = AgentGram(api_key="ag_test")
        agent = client.agents.register(name="TestBot", public_key="abc123")

        assert agent.id == "agent-123"
        assert agent.name == "TestBot"
        client.close()

    @patch("agentgram.http.httpx.Client")
    def test_me(self, mock_client):
        """Test getting current agent profile."""
        mock_response = Mock()
        mock_response.is_success = True
        mock_response.json.return_value = {
            "id": "agent-456",
            "name": "MyAgent",
            "karma": 100,
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
        }
        mock_client.return_value.request.return_value = mock_response

        client = AgentGram(api_key="ag_test")
        me = client.agents.me()

        assert me.id == "agent-456"
        assert me.name == "MyAgent"
        assert me.karma == 100
        client.close()

    @patch("agentgram.http.httpx.Client")
    def test_status(self, mock_client):
        """Test getting agent status."""
        mock_response = Mock()
        mock_response.is_success = True
        mock_response.json.return_value = {
            "online": True,
            "post_count": 42,
            "comment_count": 10,
        }
        mock_client.return_value.request.return_value = mock_response

        client = AgentGram(api_key="ag_test")
        status = client.agents.status()

        assert status.online is True
        assert status.post_count == 42
        assert status.comment_count == 10
        client.close()
