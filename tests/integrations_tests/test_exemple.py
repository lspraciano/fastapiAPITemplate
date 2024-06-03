import pytest
from httpx import AsyncClient, Response

from app.core.metadata.metadata import get_project_metadata


@pytest.mark.asyncio
async def test_root_returns_correct_status_code(
        async_client: AsyncClient
):
    project_metadata: dict = get_project_metadata()
    response: Response = await async_client.get(
        url="/",
        headers={
            "Content-Type": "application/json"
        },
    )

    assert response.status_code == 200
