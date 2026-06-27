"""Tests for envelope.py and errors.py — v2 {data, error, meta} shape."""
from cplugin_webapi_sdk.envelope import ApiEnvelope, ApiMeta, ApiErrorBody
from cplugin_webapi_sdk.errors import ApiError


def test_envelope_parses_data_error_meta():
    env = ApiEnvelope[str].model_validate(
        {"data": "2026-06-26T00:00:00Z",
         "error": None,
         "meta": {"activityId": "abc", "paging": None}}
    )
    assert env.data == "2026-06-26T00:00:00Z"
    assert env.error is None
    assert env.meta.activity_id == "abc"


def test_envelope_parses_paging():
    env = ApiEnvelope[list].model_validate(
        {"data": [], "error": None,
         "meta": {"activityId": None, "paging": {"nextCursor": "c2", "hasMore": True}}}
    )
    assert env.meta.paging.next_cursor == "c2"
    assert env.meta.paging.has_more is True


def test_apierror_surfaces_fields():
    body = ApiErrorBody.model_validate({"code": "Forbidden", "managerCode": "7", "message": "nope"})
    meta = ApiMeta.model_validate({"activityId": "trace-1", "paging": None})
    err = ApiError(body, meta, status=200)
    assert err.code == "Forbidden"
    assert err.description == "nope"
    assert err.activity_id == "trace-1"
    assert err.manager_code == "7"
    assert err.status == 200
    assert str(err) == "nope"


def test_apierror_default_message_from_code():
    body = ApiErrorBody.model_validate({"code": "Internal", "managerCode": None, "message": None})
    err = ApiError(body, None, status=200)
    assert str(err) == "v2 error: Internal"
    assert err.activity_id is None
