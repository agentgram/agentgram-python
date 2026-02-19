"""AX Score resource endpoints."""

from typing import TYPE_CHECKING, Any, List, Optional

from ..models import AXLlmsTxt, AXReportSummary, AXScanReport, AXSimulation

if TYPE_CHECKING:
    from ..http import AsyncHTTPClient, HTTPClient


class AXReportsResource:
    """Synchronous AX Score report operations."""

    def __init__(self, http_client: "HTTPClient"):
        """
        Initialize AX reports resource.

        Args:
            http_client: HTTP client instance
        """
        self._http = http_client

    def list(
        self,
        site_id: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List[AXReportSummary]:
        """
        List AX Score scan reports.

        Args:
            site_id: Filter by site ID
            page: Page number for pagination
            limit: Number of results per page

        Returns:
            List of report summaries

        Raises:
            AgentGramError: On API error
        """
        params: dict[str, Any] = {}
        if site_id is not None:
            params["siteId"] = site_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        response = self._http.get("/ax-score/reports", params=params)
        return [AXReportSummary(**report) for report in response]

    def get(self, report_id: str) -> AXScanReport:
        """
        Get a detailed AX Score scan report.

        Args:
            report_id: Report UUID

        Returns:
            Full scan report with categories and recommendations

        Raises:
            NotFoundError: If report doesn't exist
            AgentGramError: On API error
        """
        response = self._http.get(f"/ax-score/reports/{report_id}")
        return AXScanReport(**response)


class AXResource:
    """Synchronous AX Score operations."""

    def __init__(self, http_client: "HTTPClient"):
        """
        Initialize AX Score resource.

        Args:
            http_client: HTTP client instance
        """
        self._http = http_client
        self.reports = AXReportsResource(http_client)

    def scan(self, url: str, name: Optional[str] = None) -> AXScanReport:
        """
        Scan a URL for AI discoverability.

        Args:
            url: URL to scan
            name: Optional display name for the site

        Returns:
            Scan report with scores and recommendations

        Raises:
            ValidationError: If URL is invalid
            AgentGramError: On API error
        """
        data: dict[str, str] = {"url": url}
        if name is not None:
            data["name"] = name

        response = self._http.post("/ax-score/scan", json=data)
        return AXScanReport(**response)

    def simulate(
        self, scan_id: str, query: Optional[str] = None
    ) -> AXSimulation:
        """
        Run an AI simulation against a scanned site.

        This is a paid endpoint that simulates how an AI model would
        interact with and recommend the scanned site.

        Args:
            scan_id: ID of a previous scan report
            query: Optional query to simulate

        Returns:
            Simulation result with recommendation analysis

        Raises:
            NotFoundError: If scan report doesn't exist
            AgentGramError: On API error
        """
        data: dict[str, str] = {"scanId": scan_id}
        if query is not None:
            data["query"] = query

        response = self._http.post("/ax-score/simulate", json=data)
        return AXSimulation(**response)

    def generate_llms_txt(self, scan_id: str) -> AXLlmsTxt:
        """
        Generate an llms.txt file for a scanned site.

        This is a paid endpoint that generates an llms.txt file based
        on the scan results to improve AI discoverability.

        Args:
            scan_id: ID of a previous scan report

        Returns:
            Generated llms.txt content

        Raises:
            NotFoundError: If scan report doesn't exist
            AgentGramError: On API error
        """
        response = self._http.post(
            "/ax-score/generate-llmstxt", json={"scanId": scan_id}
        )
        return AXLlmsTxt(**response)


class AsyncAXReportsResource:
    """Asynchronous AX Score report operations."""

    def __init__(self, http_client: "AsyncHTTPClient"):
        """
        Initialize async AX reports resource.

        Args:
            http_client: Async HTTP client instance
        """
        self._http = http_client

    async def list(
        self,
        site_id: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List[AXReportSummary]:
        """
        List AX Score scan reports asynchronously.

        Args:
            site_id: Filter by site ID
            page: Page number for pagination
            limit: Number of results per page

        Returns:
            List of report summaries

        Raises:
            AgentGramError: On API error
        """
        params: dict[str, Any] = {}
        if site_id is not None:
            params["siteId"] = site_id
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit

        response = await self._http.get("/ax-score/reports", params=params)
        return [AXReportSummary(**report) for report in response]

    async def get(self, report_id: str) -> AXScanReport:
        """
        Get a detailed AX Score scan report asynchronously.

        Args:
            report_id: Report UUID

        Returns:
            Full scan report with categories and recommendations

        Raises:
            NotFoundError: If report doesn't exist
            AgentGramError: On API error
        """
        response = await self._http.get(f"/ax-score/reports/{report_id}")
        return AXScanReport(**response)


class AsyncAXResource:
    """Asynchronous AX Score operations."""

    def __init__(self, http_client: "AsyncHTTPClient"):
        """
        Initialize async AX Score resource.

        Args:
            http_client: Async HTTP client instance
        """
        self._http = http_client
        self.reports = AsyncAXReportsResource(http_client)

    async def scan(self, url: str, name: Optional[str] = None) -> AXScanReport:
        """
        Scan a URL for AI discoverability asynchronously.

        Args:
            url: URL to scan
            name: Optional display name for the site

        Returns:
            Scan report with scores and recommendations

        Raises:
            ValidationError: If URL is invalid
            AgentGramError: On API error
        """
        data: dict[str, str] = {"url": url}
        if name is not None:
            data["name"] = name

        response = await self._http.post("/ax-score/scan", json=data)
        return AXScanReport(**response)

    async def simulate(
        self, scan_id: str, query: Optional[str] = None
    ) -> AXSimulation:
        """
        Run an AI simulation against a scanned site asynchronously.

        This is a paid endpoint that simulates how an AI model would
        interact with and recommend the scanned site.

        Args:
            scan_id: ID of a previous scan report
            query: Optional query to simulate

        Returns:
            Simulation result with recommendation analysis

        Raises:
            NotFoundError: If scan report doesn't exist
            AgentGramError: On API error
        """
        data: dict[str, str] = {"scanId": scan_id}
        if query is not None:
            data["query"] = query

        response = await self._http.post("/ax-score/simulate", json=data)
        return AXSimulation(**response)

    async def generate_llms_txt(self, scan_id: str) -> AXLlmsTxt:
        """
        Generate an llms.txt file for a scanned site asynchronously.

        This is a paid endpoint that generates an llms.txt file based
        on the scan results to improve AI discoverability.

        Args:
            scan_id: ID of a previous scan report

        Returns:
            Generated llms.txt content

        Raises:
            NotFoundError: If scan report doesn't exist
            AgentGramError: On API error
        """
        response = await self._http.post(
            "/ax-score/generate-llmstxt", json={"scanId": scan_id}
        )
        return AXLlmsTxt(**response)
