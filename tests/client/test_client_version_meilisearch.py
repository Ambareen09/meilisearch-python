def test_get_version(client):
    """Tests getting the version of the Meilisearch instance."""
    response = client.get_version()
    assert 'pkgVersion' in response
    assert 'commitSha' in response
    assert 'commitDate' in response
