"""Quickstart: authenticate, discover platforms, read MT4 server time.

This script targets the STAGING environment so no production data is touched.
Set your credentials before running:

    export WEBAPI_CLIENT_ID=your-client-id
    export WEBAPI_CLIENT_SECRET=your-client-secret
    python examples/01_hello.py

You can obtain credentials from the CPlugin Toolbox:
    https://pre.toolbox.cplugin.com  (staging)
    https://toolbox.cplugin.com      (production)
"""
from __future__ import annotations

import os

from cplugin_webapi_sdk import ApiError, CPluginWebApiClient, paginate_sync


def main() -> None:
    # * Client uses staging by default — safe for exploration without
    # * touching production data.
    with CPluginWebApiClient(
        env="staging",
        client_id=os.environ["WEBAPI_CLIENT_ID"],
        client_secret=os.environ["WEBAPI_CLIENT_SECRET"],
    ) as client:
        # -- discover platforms -----------------------------------------------
        platforms = client.list_trade_platforms()
        if not platforms:
            print("No platforms found — check that the credential has platform access.")
            return

        print(f"Found {len(platforms)} platform(s):")
        for p in platforms:
            print(f"  {p.get('id')}  |  {p.get('name')}  |  type={p.get('type')}")

        tp = platforms[0]["id"]
        print()

        # -- MT4 server time --------------------------------------------------
        try:
            t = client.mt4.get_server_time(tp)
            print("MT4 server time:", t)
        except ApiError as err:
            print(f"API error [{err.code}]: {err.description}")
            if err.activity_id:
                print("  Activity ID:", err.activity_id)

        # -- pagination example -----------------------------------------------
        # * paginate_sync yields one page (list of items) per iteration.
        # * Each page's items are streamed without loading the full dataset.
        print()
        print("First page of MT4 users (limit=5):")
        for page in paginate_sync(lambda cur: client.mt4.users_request(tp, cursor=cur, limit=5)):
            for user in page:
                print(f"  login={user.get('login')}  group={user.get('group')}")
            break  # * only the first page for this quickstart demo


if __name__ == "__main__":
    main()
