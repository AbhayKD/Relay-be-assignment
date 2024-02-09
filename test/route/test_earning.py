import pytest
import json

REQUEST_BODY = [
    {
        "route_id": "RT5QHQ6M3A937H",
        "attempt_date_time": "2023-12-18T08:33:18.588934+00:00",
        "success": True,
    },
    {
        "route_id": "RT5QHQ6M3A937H",
        "attempt_date_time": "2023-12-18T08:37:11.897203+00:00",
        "success": True,
    },
    {
        "route_id": "RT5QHQ6M3A937H",
        "attempt_date_time": "2023-12-18T08:39:10.938613+00:00",
        "success": True,
    },
    {
        "route_id": "RT5QHQ6M3A937H",
        "attempt_date_time": "2023-12-18T08:43:14.747595+00:00",
        "success": False,
    },
    {
        "route_id": "RT5QHQ6M3A937H",
        "attempt_date_time": "2023-12-18T08:45:45.375317+00:00",
        "success": True,
    },
    {
        "route_id": "RT5QHQ6M3A937H",
        "attempt_date_time": "2023-12-18T08:45:58.396736+00:00",
        "success": True,
    },
]
# Example payloads
payloads = [
    (
        REQUEST_BODY,
        "platinum_tier",
        {
            "line_items": [
                {
                    "name": "Per successful attempt",
                    "quantity": 5.0,
                    "rate": 0.667,
                    "total": 3.335,
                },
                {
                    "name": "Per unsuccessful attempt",
                    "quantity": 1.0,
                    "rate": 0.155,
                    "total": 0.155,
                },
                {"name": "Long route bonus", "quantity": 0, "rate": 12.0, "total": 0.0},
                {
                    "name": "Loyalty Bonus (attempts)",
                    "quantity": 0,
                    "rate": 19.0,
                    "total": 0.0,
                },
                {
                    "name": "Consistency Bonus",
                    "quantity": 0,
                    "rate": 32.0,
                    "total": 0.0,
                },
            ],
            "line_item_subtotal": 3.4899999999999998,
            "hours_worked": 0.2110577227777778,
            "minimum_earnings": 3.218630272361111,
            "final_earnings": 3.4899999999999998,
        },
    ),
    (
        REQUEST_BODY,
        "gold_tier",
        {
            "line_items": [
                {
                    "name": "Per successful attempt",
                    "quantity": 5.0,
                    "rate": 0.511,
                    "total": 2.555,
                },
                {
                    "name": "Per unsuccessful attempt",
                    "quantity": 1.0,
                    "rate": 0.126,
                    "total": 0.126,
                },
                {
                    "name": "Consistency Bonus",
                    "quantity": 0,
                    "rate": 32.0,
                    "total": 0.0,
                },
            ],
            "line_item_subtotal": 2.681,
            "hours_worked": 0.2110577227777778,
            "minimum_earnings": 3.1658658416666667,
            "final_earnings": 3.1658658416666667,
        },
    ),
    (
        REQUEST_BODY,
        "silver_tier",
        {
            "line_items": [
                {
                    "name": "Per successful attempt",
                    "quantity": 5.0,
                    "rate": 0.65,
                    "total": 3.25,
                },
                {
                    "name": "Per unsuccessful attempt",
                    "quantity": 1.0,
                    "rate": 0.0,
                    "total": 0.0,
                },
                {
                    "name": "Loyalty Bonus (attempts)",
                    "quantity": 0,
                    "rate": 19.0,
                    "total": 0.0,
                },
                {"name": "Quality Bonus", "quantity": 0, "rate": 25.0, "total": 0.0},
            ],
            "line_item_subtotal": 3.25,
            "hours_worked": 0.2110577227777778,
            "minimum_earnings": 2.8492792575,
            "final_earnings": 3.25,
        },
    ),
    (
        REQUEST_BODY,
        "bronze_tier",
        {
            "line_items": [
                {
                    "name": "Per successful attempt",
                    "quantity": 5.0,
                    "rate": 0.459,
                    "total": 2.295,
                },
                {
                    "name": "Per unsuccessful attempt",
                    "quantity": 1.0,
                    "rate": 0.229,
                    "total": 0.229,
                },
                {"name": "Long route bonus", "quantity": 0, "rate": 10.0, "total": 0.0},
                {
                    "name": "Loyalty Bonus (routes)",
                    "quantity": 0,
                    "rate": 20.0,
                    "total": 0.0,
                },
            ],
            "line_item_subtotal": 2.524,
            "hours_worked": 0.2110577227777778,
            "minimum_earnings": 3.060336980277778,
            "final_earnings": 3.060336980277778,
        },
    ),
]


@pytest.mark.parametrize("body, rate_card_id, expected_response", payloads)
class TestEarning:
    def test_get_user(self, client, body, rate_card_id, expected_response):
        response = client.post(f"/earning/{rate_card_id}", json=body)
        assert response.status_code == 200
        result = json.loads(response.data.decode("utf-8"))
        print(result)
        assert result == expected_response
