"""Requests"""
import requests

from requests_oauth2client import OAuth2Client, OAuth2ClientCredentialsAuth

BASE_URL = "https://play.endpointcloudservices.infra-host.com"
CLIENT_ID = "a5ta6oue1vt9cib4ggov7spr9"
CLIENT_SECRET = "" # need to fill this in AND NOT COMIT - what's the best practice here?
SCOPE = "ccss/access"

def oauth2_session(client_id, client_secret, base_url, scope) -> requests.Session:
    """ Handle OAuth 2 ClientID grant type"""
    token_url = f"{base_url}/oauth2/token" # This may be different for your endpoint

    oauth2client = OAuth2Client( token_endpoint=token_url, client_id=client_id, client_secret=client_secret)
    auth = OAuth2ClientCredentialsAuth( oauth2client, scope=scope)

    session = requests.Session()
    session.auth = auth
    return session

def test_get_partitions_from_account() -> None:
    """My first test"""
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.get(f"{BASE_URL}/api/v2/accounts/yGI26YFO/partitions")
    print(response)
    assert response.status_code == 200

def test_get_partition_directly() -> None:
    """My first test"""
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.get(f"{BASE_URL}/api/v2/partitions/yGI26YFO.XtJTuX0M")
    print(response)
    assert response.status_code == 200

def test_get_manifests_from_partition() -> None:
    """My second test"""
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.get(f"{BASE_URL}/api/v2/partitions/yGI26YFO.XtJTuX0M/manifests")
    print(response.json)
    assert response.status_code == 200

def test_get_vulnerability_from_partition() -> None:
    """My second test"""
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.get(f"{BASE_URL}/api/v2/partitions/yGI26YFO.XtJTuX0M/vulnerabilities")
    print(response.json)
    assert response.status_code == 200

def test_get_vulnerability_from_partition_local() -> None:
    """My second test"""
    local_base_url = "http://localhost:8080"
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.get(f"{local_base_url}/api/v2/partitions/yGI26YFO.XtJTuX0M/vulnerabilities")
    print(response.json)
    assert response.status_code == 200

def test_get_processed_from_partition() -> None:
    """My second test"""
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.get(f"{BASE_URL}/api/v2/partitions/yGI26YFO.XtJTuX0M/processed")
    print(response.json)
    assert response.status_code == 200

def test_get_processed_from_partition_local() -> None:
    """My second test"""
    local_base_url = "http://localhost:8080"
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.get(f"{local_base_url}/api/v2/partitions/yGI26YFO.XtJTuX0M/processed")
    print(response.json)
    assert response.status_code == 200


def test_get_vulnerability_from_device() -> None:
    """My second test"""
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.get(f"{BASE_URL}/api/v2/devices/yGI26YFO.XtJTuX0M.9Y4iPsoCpnzc0KVf/vulnerabilities")
    print(response.json)
    assert response.status_code == 200

def test_post_manifests_to_partition() -> None:
    """My third test"""
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.post(f"{BASE_URL}/api/v2/partitions/yGI26YFO.XtJTuX0M/manifests",
                               headers={"Accept": "application/json"},
                               json=[{"_id":0}])
    assert response.status_code == 202

def test_post_manifests_to_device() -> None:
    """My nth test"""
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.post(f"{BASE_URL}/api/v2/devices/yGI26YFO.XtJTuX0M.9Y4iPsoCpnzc0KVf/manifests",
                               headers={"Accept": "application/json"},
                               json=[{"_id":0}])
    assert response.status_code == 202

def test_post_manifests_to_partition_local() -> None:
    """My third test"""
    local_base_url = "http://localhost:8080"
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    response = my_session.post(f"{local_base_url}/api/v2/partitions/yGI26YFO.XtJTuX0M/manifests",
                               headers={"Accept": "application/json"},
                               json=[{"_id":0}])
    print(response.text)
    assert response.status_code == 202

def test_docs_local() -> None:
    """My nth test"""
    # Create a session
    local_base_url = "http://localhost:8080"

    # Use it as normal requests object to post and get
    response = requests.get(f"{local_base_url}/docs",
                               json={"_id":0},
                               timeout=60)
    assert response.status_code == 200

def test_health_local() -> None:
    """My nth test"""

    local_base_url = "http://localhost:8080"
    my_session = oauth2_session(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                base_url=BASE_URL,
                                scope=SCOPE)

    # Use it as normal requests object to post and get
    response = my_session.get(f"{local_base_url}/api/v2/health",
                               json={"_id":0},
                               timeout=60)
    assert response.status_code == 200
