# from utils import remote_system_check
# from utils.remote_system.check import check_remote_system
from utils.remote_system_check import check_remote_system_health


def main() -> list[str]:
    server_list = [
        {"ip_address": "ip_address_1",
            "username": "admin", "password": "password123"},
        {"ip_address": "ip_address_2",
         "username": "admin", "password": "password123"},
    ]

    Response: list = []

    for server in server_list:
        hostname, username, password = server["ip_address"], server["username"], server["password"]
        result = check_remote_system_health(
            hostname, username, password)
        Response.append(result)

    return Response


if __name__ == "__main__":
    results = main()
    for res in results:
        print(res)
