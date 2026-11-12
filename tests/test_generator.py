from retailflow.data_generation import generate_raw_data
def test_generator_is_deterministic_and_contains_defects(tmp_path):
    counts = generate_raw_data(tmp_path)
    assert counts["orders"] == 91
    assert "not-a-timestamp" in (tmp_path / "orders.csv").read_text()
    assert (tmp_path / "website_events.json").read_text().count("event_id") == 150
